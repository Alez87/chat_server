The provided answer is based on socket communications between server and telnet clients.  
Every client that connects to the server creates a thread to handle the communication.  

How to run the code:  
- > on server: python3 chat_server.py
- > on each client: telnet <ip> 10000 (e.g. telnet 127.0.0.1 10000)

Automated test code inside the file 'unittest_chatserver.py'  
To run the automated test, execute the file:  
> python3 unittest_chatserver.py

Code tested on Python 3.7.3.
