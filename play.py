#!/usr/bin/env python 
#coding:utf-8

age = 23
count = 0

for i in range(10):
	if count < 3:
		a = int(input("Plz input num: "))
		if a == age:
			print("恭喜你，答对了！")
			break
		elif a > age:
			print("猜大了")
		else:
			print("猜小了")
	else:
		b = input("太笨了，还继续玩吗？(yes or not）:")
		if b == "yes":
			count = 0 
			continue
		else:
			print("Bye")

	count += 1
