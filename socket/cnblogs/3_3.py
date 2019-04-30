#!/usr/bin/env python 
#coding=utf-8

import socket 
import os

sc = socket.socket()
sc.connect(('127.0.0.1', 8080))

res = sc.recv(1024)
res_str = str(res)
print "res is: %s" % res

size = os.stat("1_1.py").st_size
sc.sendall(bytes(str(size)))
sc.recv(1024)

with open("1_1.py","r+") as f:
	for line in f:
		sc.sendall(line)
