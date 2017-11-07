#!/usr/bin/env python
#

import socket

def getRemoteIp():
	remoteHost = 'www.python.org'
	try:
		print 'IP address of', remoteHost,': %s' % socket.gethostbyname(remoteHost)
	except socket.error, err_msg:
		print '%s: %s' % (remoteHost,err_msg)

if __name__ == '__main__':
	getRemoteIp()	
		
