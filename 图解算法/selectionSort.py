#!/usr/bin/env python
"""
选择排序算法
"""
def findSmallest(arr):
    smallest = arr[0]   # 存储最小的值
    smallest_index = 0  # 存储最小元素的索引

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort([5, 4, 6, 2, 10]))
