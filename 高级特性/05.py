#coding: utf-8

import re
from pyquery import PyQuery as pq

fp = open('/Users/lianzhen/Desktop/hh.html', 'r')
fc = fp.read()
# print(fc)

with open('/Users/lianzhen/Desktop/hhh.html', 'w', encoding='utf-8') as f:
    f.write(fc)

doc = pq(filename='/Users/lianzhen/Desktop/hhh.html')
# print(doc('p'))
text = re.findall('<.*?>(.*)</.*?>', fc)
print(text)


