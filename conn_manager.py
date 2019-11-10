import socket
from threading import Thread, Lock
import constants as c
import logging

clients_connected = []

class ConnManager(Thread):
#    clients_connected = []
    mutex = Lock()
    log = None

    def __init__(self, socket, ip, port):
        Thread.__init__(self)
        self.socket = socket
        self.ip = ip
        self.port = port

    def run(self):
        self.new_client()
        try:
            while True:
                data = self.socket.recv(c.BYTE_TO_RECEIVE)
                data_str = data.decode(c.ENCODING)
                self.log.info('From client ' + str(self.ip)+':'+str(self.port) + ' data received: ' + data_str)
                if data_str.rstrip() == c.EXIT_COMMAND:
                    break
                for client in clients_connected:
                    if client.socket != self.socket:
                        client.socket.send(data)
        except:
            self.log.error("Server has closed the connection.")
        self.close()

    def get_clients(self):
        return clients_connected

    def set_log(self, log):
        self.log = log

    def new_client(self):
        self.mutex.acquire()
        clients_connected.append(self)
        self.mutex.release()
        self.log.info('%s:%s connected.' % (self.ip,self.port))

    def close(self):
        self.socket.close()
        self.mutex.acquire()
        try:
            clients_connected.remove(self)
            self.log.info('%s:%s disconnected.' % (self.ip, self.port))
        except ValueError as e:
            self.log.error("Connection already closed by the server.")
        self.mutex.release()
