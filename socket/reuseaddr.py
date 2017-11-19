#!/usr/bin/env pyton 
#

import socket
import sys

def reuse_socket_addr():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# get old socket state
	old_state = s.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
	print "old socket state: %s" % old_state

	# enable reuseaddr option 
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	
	# get new socket state 
	new_state = s.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
	print "new socket state: %s" % new_state

	local_port = 8282
	
	srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	srv.bind(('',local_port))
	srv.listen(1)
	print "Listening on port: %s" % local_port
	while True:
		try:
			connection, addr = srv.accept()
			print 'connected by %s:%s' % (addr[0], addr[1])
		except KeyboardInterrupt:
			break
		except socket.error, msg:
			print '%s' % (msg,)

if __name__ == '__main__':
	reuse_socket_addr()
