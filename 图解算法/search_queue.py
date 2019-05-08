#!/usr/bin/env python
#coding=utf-8

from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def search(name):
    search_queue = deque()        # 创建一个队列
    search_queue += graph["you"]  # 将你的邻居都加入到这个搜索队列中
    searched = []                 # 这个数组用于记录检查过的人

    while search_queue:
        person = search_queue.popleft()   # 就取出其中的第一个人
        if not person in searched:        # 仅当这个人没检查过时才检查
            if person_is_seller(person):      # 检查这个人是否是芒果销售商
                print(person + ' is a mongo celler!')
                return True
            else:
                search_queue += graph[person]  # 还是芒果销售商。将这个人的朋友都加入搜索队列
                searched.append(person)        # 将这个人标记为检查过

    return False  # 如果到达了这里，就说明队列中没人是芒果销售商


def person_is_seller(name):
    return name[-1] == 'm'

search("you")

















