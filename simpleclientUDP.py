#!/usr/bin/python3

import socket

# Create a socket for UDP over IPv6
s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM )

# port to send to and the v6 address of destination (localhost)
port = 5005
ip = '::1'

# send data - note sendto uses the destination ip, port as there is no connection
s.sendto(b'Hello, server', (ip, port))

# receive response
# <Your Code Here>
