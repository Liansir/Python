#!/usr/bin/env python 
#
import socket

HOST = ''
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connected conn [%s] by addr [%s]' % (conn,addr)
while 1:
	data = conn.recv(1024)
	print 'data is: ', data
	if not data: break
	conn.sendall(data)
	print 'conn_sendall is: ', conn.sendall(data)
conn.close()
