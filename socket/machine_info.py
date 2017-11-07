#!/usr/bin/env python
#

import socket

def printMacheInfo():
	hostName = socket.gethostname()
	ipAddress = socket.gethostbyname(hostName)

	print 'Host name: %s' % hostName
	print 'IP address: %s' % ipAddress

if __name__ == '__main__':
	printMacheInfo()

