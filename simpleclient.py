#!/usr/bin/python3

# Import socket module
import socket
from socket import AF_INET6
s = socket.socket(AF_INET6)

# Define the port on which you want to connect
port = 5000

# connect to the server on local computer
s.connect(('::1', port))

# receive data from the server
print(s.recv(1024))

# close the connection
s.close()
