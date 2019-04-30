#!/usr/bin/env python 
#coding=utf-8

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', 8080))
sock.listen(5)

print '等待客户端连接...'

(client,(ip,port)) = sock.accept()

print '建立起一个连接，对方IP为：', ip 

print '建立起一个port, port为：', port 

print 'client为：', client

print '开始接收数据...'

data = 'start'

while len(data):
	data = client.recv(1024)
	print '接收到的数据：', data
	client_send =client.send('return data:' +data)
	print 'client_send: ', client_send
	

print '关闭连接...'
client.close()

print '关闭服务...'
tcpsock.close()
