#!/usr/bin/env python 
#

import socket
import sys
import argparse

host = '127.0.0.1'

def echo_client(port):
	"""A simple echo client"""
	# create a tcp/ip socket
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# connect the socket to the server
	server_address = (host, port)
	print "Connecting to %s port %s" % server_address
	s.connect(server_address)

	# send data
	try:
		# send data
		message = "test message, this will be echoed"
		print "sending %s" % message
		s.sendall(message)
		# lock for the response
		amount_received = 0
		amount_expected = len(message)
		while amount_received < amount_expected:
			data = s.recv(16)
			amount_received += len(data)
			print "received: %s" % data
	except socket.error, e:
		print "socket error: %s" % str(e)
	except Exception, e:
		print "other exception: %s" % str(e)
	finally:
		print "closing connection to the server"
		s.close()

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Socket Server Exception')
	parser.add_argument('--port',action="store",dest="port",type=int,required=True)
	args = parser.parse_args()
	port = args.port
	echo_client(port)
