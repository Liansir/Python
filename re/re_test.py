#!/usr/bin/evn python 
#coding:utf-8

"""
运行此脚本前先运行genlog.py, 并将输出重写向到文件trans.log
"""
import re

list2 = []
list3 = []

with open('./trans.log', 'r') as f:
    list1 = f.readlines()
    for line in list1:
        obj = re.search(r'(.*?),(.*?),.*', line, re.M|re.I)
        if obj:
            print("obj_type is matched: ",obj.group(1))
            print("obj_dest is matched: ",obj.group(2))
            list2.append(obj.group(1))
            list3.append(obj.group(2))

list5 = []
list6 = []

with open('./trans.log','r') as f:
    list4 = f.readlines()
    for line in list4:
        obj = re.search(r'.*?,(.*?),(.*?),.*', line, re.M|re.I)
        if obj:
            print("obj_typex is matched: ", obj.group(1))
            print("obj_delay is matched: ", obj.group(2))
            list5.append(obj.group(1))
            list6.append(obj.group(2))


n1 = range(0, len(list2))
n2 = range(0, len(list5))
for i in n1:
    for j in n2:
        with open('/root/pytest/node_status.txt','a+') as f:
            if list3[i] == list5[j]:
                node_status = list2[i] +' ' + list6[j]
                f.write(node_status + '\n')
