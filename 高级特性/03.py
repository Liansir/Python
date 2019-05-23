from pyquery import PyQuery as pq
import codecs

fp = open('/Users/lianzhen/Desktop/hh.html', 'r')
fc = fp.read()
doc2 = pq(filename=fc)
p2 = doc2('p')
text2 = p2.text()
with open('协议详情2.txt', 'w', encoding='utf-8') as f:
    f.write(text2)


print(p2.text())