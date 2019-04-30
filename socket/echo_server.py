#!/usr/bin/env python
#

import socket
import sys
import argparse

host = 'localhost'
data_payload = 2048
backlog = 5

def echo_server(port):
	"""A simple echo server"""
	# Create a tcp socket
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# Enable reuser address/port
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	# Bind to the port
	server_address = (host, port)
	print "Starting echo server on %s port %s" % server_address
	# Listen to client
	s.listen(backlog)
	while True:
		print "Waiting to receive message from client"
		client, address = s.accept()
		data = client.recv(data_paylod)
		if data:
			print "Data: %s" % data
			client.send(data)
			print "send %s bytes back to %s" % (data, address)
		# close connection 
		client.close()
	
if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Socket Server Example")
	parser.add_argument('--port',action="store",dest="port",type=int,required=True)
	args = parser.parse_args()
	port = args.port
	echo_server(port)
