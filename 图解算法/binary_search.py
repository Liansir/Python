#!/usr/bin/env python 

import random

def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = list[mid]
        if guess == item:
            print('猜对了, 我在列表中的索引是{}, 我是{}'.format(mid, list[mid]))
            return mid 
        if guess > item:
            print('猜大了')
            high = mid - 1
        else:
            print('猜小了')
            low = mid + 1
    return None

my_list = [i for i in range(100) if i % 2 ]
print(my_list)
binary_search(my_list, 9)



