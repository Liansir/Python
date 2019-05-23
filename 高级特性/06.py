from pyquery import PyQuery as pq

doc = pq(filename=open('h.html', encoding='utf-8'))
print(doc('p'))