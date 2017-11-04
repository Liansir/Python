#!/usr/bin/env python
#

def stat(name,**score):
	print(name)
	print(score)
	print('%s的平均成绩为%2.f' %(name,sum(score.values())/len(score)))

stat('Tom',MATH=90,English=32,Chinese=100)

#关键字参数以(**)标识，并以字典的形式传递给函数
