'''
利用time函数，生成两个函数，顺序调用，计算总的运行时间
'''

import time
import _thread as thread

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
    # 启动多线程的意思是用多线程去执行某个函数
    # 启动多线程函数为start_new_thread
    # 参数两个，一个是需要运行的函数名，第二个是函数的参数作为无组使用, 为空则使用空无组
    # 注意: 如果函数只有一个参数, 需要参数后有一个逗号
    thread.start_new_thread(loop1, ('维莉',))
    thread.start_new_thread(loop2, ('美幸', '文慧'))

    print('All done at: ', time.ctime())

if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)