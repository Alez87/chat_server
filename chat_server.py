import logging
import socket
import sys
from conn_manager import ConnManager

import constants as c

log = logging.getLogger()

def setup_log():
    log.setLevel(c.LOG_LEVEL)
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s]: %(message)s"))
    log.addHandler(handler)

def get_socket():
    return server_socket

def close_socket(server_socket):
    server_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((c.IP, c.PORT))
    server_socket.listen(5)
    log.info("Server is listening on port " + str(c.PORT))
    manager = None
    try:
        while True:
            connection, address = server_socket.accept()
            ip = address[0]
            internal_port = address[1]
            manager = ConnManager(connection, ip, internal_port)
            manager.set_log(log)
            manager.daemon = True
            manager.start()
    except:
        log.error(sys.exc_info())
        close_socket(server_socket)
        print('Closing the server.')
        sys.exit(0)

if __name__ == "__main__":
    setup_log()
    main()
