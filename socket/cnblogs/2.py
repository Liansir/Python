#!/usr/bin/env python 
#
import SocketServer

class Myserver(SocketServer.BaseRequestHandler):
	def handle(self):
		conn = self.request
		conn.sendall("hello, I'm jiqiren")
		while True:
			res = conn.recv(1024)
			if res == "q":
				break
			conn.sendall("ni hao")

if __name__ == '__main__':
	server = SocketServer.ThreadingTCPServer(('127.0.0.1',8080),Myserver)
	server.serve_forever()
