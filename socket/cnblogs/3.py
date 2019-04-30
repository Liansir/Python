#!/usr/bin/env python 
#coding=utf-8

import socket 

s = socket.socket()
s.bind(('127.0.0.1',8080))
s.listen(5)

while True:
	conn, address = s.accept()
	conn.sendall("欢迎光临自如")

	size = conn.recv(1024)
	file_size = int(size)

	conn.sendall("开始传送")
	has_size = 0
	f = open("1.py","w+")
	while True:
		if file_size == has_size:
			break
		date = conn.recv(1024)
		f.write(date)
		has_size += len(date)

	f.close()

