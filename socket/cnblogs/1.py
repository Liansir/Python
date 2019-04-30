#!/usr/bin/env python 

import socket 

s = socket.socket()
s.bind(('127.0.0.1', 8080))
s.listen(5)

conn, address = s.accept()
s.sendall('Hello world')
