#!/usr/bin/env python 
#

def login(username,password):
	'''
	用户登陆
	return: true表示成功，false表示失败
	'''

	f = open('db','r')
	for line in f:
		line_list = line.strip().split('|')
		if line_list[0] == username and line_list[1] == password:
			return True
	
	return False

def register(username,password):
	'''
	用户注册
	return: 默认返回None
	'''
	f = open('db','a')
	temp = '\n' + username + '|' + password
	f.write(temp)
	f.close()

def main():
	t = input("1: 登陆；2：注册")
	if t == '1':
		user = input("请输入用户名: ")
		pwd = input("请输入密码: ")
		r = login(user,pwd)
		if r:
			print('登陆成功')
		else:
			print('登陆失败')
	elif t == '2':
		user = input("请输入用户名：")
		pwd = input("请输入密码：")
		register(user,pwd) 
		print('注册成功')

if __name__ == '__main__':
	main()
