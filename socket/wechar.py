#!/usr/bin/env python 
#coding=utf-8

import socket
import select
import cPickle
import sys
import signal
import argparse
import struct 

SERVER_HOST = 'localhost'
CHAR_SERVER_NAME = 'server'

def send(channel, *args):
	buffer = cPickle.dumps(args)
	value = socket.htonl(len(buffer))
	size = struct.pack("L", value)
	channel.send(size)
	channel.send(buffer)

def receive(channel):
	size = struct.calcsize("L")
	size = channel.recv(size)
	try:
		size = socket.ntohl(struct.unpack("L", size)[0]
	except struce.error as e:
		return ''
	buf = ""
	while len(buf) < size:
		buf += channel.recv(size - len(buf))
	return cPickle.loads(buf)[0]
