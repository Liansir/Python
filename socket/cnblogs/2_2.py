#!/usr/bin/env python 
#

import socket 

sc = socket.socket()
sc.connect(('127.0.0.1',8080))

res = sc.recv(1024)
print res

while True:
	plz_input = input("hello, \n>>>")
	if plz_input == "q":
		sc.sendall(plz_input)
		break
	else:
		sc.sendall(plz_input)
		res = sc.recv(1024)
		print "res is: ", res
