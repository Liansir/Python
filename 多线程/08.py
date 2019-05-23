import time
import threading


def loop1():
    # ctime, 得到当前时间
    print('Start loop 1 at: ', time.ctime())
    time.sleep(4)
    print('End loop 1 at', time.ctime())


def loop2():
    print('Start loop 2 at: ', time.ctime())
    time.sleep(2)
    print('End loop2 at', time.ctime())

def loop3():
    print('Start loop 3 at: ', time.ctime())
    time.sleep(5)
    print('End loop3 at', time.ctime())


def main():
    print('Starting at: ', time.ctime())

    t1 = threading.Thread(target=loop1, args=())
    t1.setName('T1')
    t1.start()

    t2 = threading.Thread(target=loop2, args=())
    t2.setName('T2')
    t2.start()

    t3 = threading.Thread(target=loop3, args=())
    t3.setName('T3')
    t3.start()

    # t1.join()
    # t2.join()
    # t3.join()
    # 预期3秒后， thread2已经自动结束
    time.sleep(3)
    # enumerate 得到正在运行子线程，即子线程1和子线程3
    for thr in threading.enumerate():
        print('正在运行的线程名称是：{0}'.format(thr.getName()))

    print('存在运行的子数量为： {0}'.format(threading.activeCount()))
    print('存在运行的子数量为： {0}'.format(threading.active_count()))
    print('All done at: ', time.ctime())

if __name__ == '__main__':
    main()
