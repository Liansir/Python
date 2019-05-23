def sim_coroutine():
    print('-> start')
    x = yield
    print('-> recived', x)

# 主线程
sc = sim_coroutine()
print(111)
# 可以使用sc.send(None), 效果一样

# 预激
next(sc)

print(222)
sc.send('meixing')
