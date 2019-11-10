import unittest
import telnetlib
import time
import importlib
import threading

import constants as c

TARGET = importlib.import_module('chat_server')
socket_server = None

def chat_server():
    socket_server = TARGET.main()

class TestTelnet(unittest.TestCase):

    def test_two_telnetclient(self):
        client1 = telnetlib.Telnet(c.CLIENT_IP, c.PORT)
        client2 = telnetlib.Telnet(c.CLIENT_IP, c.PORT)
        time.sleep(1)
        client1.write(b'prova' + b'\n\r')
        line1 = client1.read_very_eager()
        line2 = client2.read_until(b'\n')
        message1 = line1.decode(c.ENCODING).rstrip()
        message2 = line2.decode(c.ENCODING).rstrip()
        self.assertTrue(message1 == '')
        self.assertTrue(message2 == 'prova')

    def test_three_telnetclient(self):
        client1 = telnetlib.Telnet(c.CLIENT_IP, c.PORT)
        client2 = telnetlib.Telnet(c.CLIENT_IP, c.PORT)
        client3 = telnetlib.Telnet(c.CLIENT_IP, c.PORT)
        time.sleep(1)
        client1.write(b'prova' + b'\n\r')
        line1 = client1.read_very_eager()
        line2 = client2.read_until(b'\n')
        line3 = client3.read_until(b'\n')
        message1 = line1.decode(c.ENCODING).rstrip()
        message2 = line2.decode(c.ENCODING).rstrip()
        message3 = line3.decode(c.ENCODING).rstrip()
        self.assertTrue(message1 == '')
        self.assertTrue(message2 == 'prova')
        self.assertTrue(message3 == 'prova')

if __name__ == '__main__':
    test = threading.Thread(target=chat_server, daemon=True)
    test.start()
    unittest.main(argv=['TestTelnet'])
    test.join()
    socket_server.socket_close()
