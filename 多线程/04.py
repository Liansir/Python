'''
利用time函数，生成两个函数，顺序调用，计算总的运行时间
'''
import time
import threading

def loop1(in1):
    # ctime, 得到当前时间
    print('Start loop 1 at: ', time.ctime())
    print('我是参数 ', in1)
    time.sleep(4)
    print('End loop 1 at', time.ctime())


def loop2(in1, in2):
    print('Start loop 2 at: ', time.ctime())
    print('我是参数 ', in1, '和参数', in2)
    time.sleep(2)
    print('End loop2 at', time.ctime())


def main():
    print('Starting at: ', time.ctime())
    t1 = threading.Thread(target=loop1, args=('维莉', ))
    t1.start()
    t2 = threading.Thread(target=loop2, args=('美幸', '文慧'))
    t2.start()
    print('All done at: ', time.ctime())

if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)