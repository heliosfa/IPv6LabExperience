#!/usr/bin/python3

# simple examples of using DNS to get host IPs
import socket
try:
    domain='www.imperial.ac.uk'
    # get the IP addresses of a host name
    # ip = socket.gethostbyname('www.soton.ac.uk')
    print("getaddrinfo() for " + domain)
    ip4 = socket.getaddrinfo(domain, None, socket.AF_INET, 0, socket.IPPROTO_UDP)
    print("IPv4: " + str([entry[4] for entry in ip4]))
    ip6 = socket.getaddrinfo(domain, None, socket.AF_INET6, 0, socket.IPPROTO_UDP)
    print("IPv6: " + str([entry[4] for entry in ip6]))
except Exception as e:
    print('error: {}'.format(e))
