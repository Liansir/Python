#!/usr/bin/env python 

import socket 

sc = socket.socket()
sc.connect(('127.0.0.1', 8080))

res = sc.recv(1024)
print "res is %s: " % res
