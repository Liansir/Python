#/usr/bin/env python
#
import re
s1 = '''
name:sim,Gender:f,
age:27,address:Jiangsu,
Edu,yjs
'''

keys = re.findall(r'([a-z]+):',s1,re.I)
values = re.findall('\w:(\w+)',s1)
print('打印')
print(keys,values)

#将键值匹配存入字典
mydict={}
for i in list(range(0,len(keys))):
    mydict[keys[i]] = values[i]

print('存入字典')
print(mydict)
