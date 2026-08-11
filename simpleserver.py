#!/usr/bin/python3

import socket
from socket import AF_INET6

# make a socket object
s = socket.socket(AF_INET6)

port = 5000

# bind to the port - empty means all interfaces
s.bind(('', port))

# listening
s.listen(5)
print ("socket is listening")

while True:

    # Establish connection with client.
    c, addr = s.accept()
    print ('Got connection from', addr )

    # send a thank you message to the client.
    c.send(b'Thank you for connecting')

    # Close the connection with the client
    c.close()
