from pyquery import PyQuery as pq

doc1 = pq(filename='/Users/lianzhen/Desktop/h.html')
p1 = doc1('p')
text1 = p1.text()
with open('协议详情.txt', 'w') as f:
    f.write(text1)

print(p1.text())
