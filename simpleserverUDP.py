#!/usr/bin/python3

import socket

# make a v6 UDP socket
s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)

port = 5005
ip = ''

# bind to the port and local host
s.bind((ip, port))

print("server waiting for UDP packets")
while True:
    # listen for a message
    data, addr = s.recvfrom(1024)
    print('Got packet from ', addr)
    print('Received %s' % data)

    # send a response
    # <Your Code Here>
