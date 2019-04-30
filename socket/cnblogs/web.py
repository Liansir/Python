#!/usr/bin/env python 
#coding:utf-8

import socket

def handle_request(client):
	buf = client.recv(1024)
	client.send("HTTP/1.1 200 OK\r\n\r\n")
	client.send("Hello World")

def main():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(('localhost',8080))
	s.listen(5)

	while True:
		conn, address = s.accept()
		handle_request(conn)
		conn.close()

if __name__ == '__main__':
	main()
