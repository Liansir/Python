#!/usr/bin/env python 
#

def func1(income,outcome,*name):
	print(income)
	print(outcome)
	print(name)
	print('一共%d口人' % len(name))
	print('人均收入为%.2f' % (income/len(name)))

func1(20000,5000,'张三','李四','王五')

#可变参数是以(*)标识，并以元组的形式传给函数


