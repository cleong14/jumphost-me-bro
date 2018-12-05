#!/usr/bin/env python

import socket

target_host = '104.248.191.147'
target_port = 80

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# send some data
client.sendto("DATA",(target_host,target_port))

# receive some data

data, addr = client.recvfrom(4096)

print('DATA', data)