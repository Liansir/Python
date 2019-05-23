#/usr/bin/env python
#coding=utf-8

import threading
import time

# Python2
# form Queue import Queue

# Python3
import queue

class Producer(threading.Thread):
    def run(self):
        global queue
        count = 0
        while True:
            if queue.qsize() < 10:
                for i in range(5):
                    count = count + 1
                    msg = '生成产品' + str(count)
                    # put是往queue里面放入一个值
                    queue.put(msg)
                    print(msg)
            time.sleep(0.5)

class Consumer(threading.Thread):
    def run(self):
        global queue
        while True:
            if queue.qsize() > 10:
                for i in range(2):
                    # get是从queue中取出一个值
                    msg = self.name + '消费了' + queue.get()
                    print(msg)
            time.sleep(1)

if __name__ == '__main__':
    queue = queue.Queue()

    for i in range(8):
        queue.put('初始产品' + str(i))
    for i in range(2):
        p = Producer()
        p.start()
    for i in range(4):
        c = Consumer()
        c.start()
