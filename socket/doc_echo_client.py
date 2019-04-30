#!/usr/bin/env python 
#
import socket

HOST = 'localhost'
PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall('HELLO WORLD')
data = s.recv(1024)
#pritn 'data: ',data
s.close()
print 'Received', repr(data)
