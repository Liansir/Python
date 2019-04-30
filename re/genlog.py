#!/usr/bin/env python 
#coding:utf-8

"""
random.randint,random.choice,random.uniform,random.sample
time.localtime,time.strftime
"""

import random
import time 

start_time = time.time()

def get_trans_type():
    sap_type = random.sample('AHCD',3)
    sun_type = ''.join(sap_type)
    return "T3HN005%s%02d" % (sun_type, random.randint(1,21))

def get_trans_source():
    return random.choice(['北京','西安','上海','广州','深圳','海南','郑州','重庆','武汉',\
                          '新疆','沈阳','兰州','西宁','长沙','新郑','浙江','南京','福建'])
def get_trans_duration():
    return random.randint(150,300)/1000.0

def get_trans_code():
    return random.choice(("0","0","0","0","0","0","0","0","0","0","0","0","0","0","1","2009"))

def get_trans_start_time():
    global start_time
    start_time += random.uniform(0,0.8) 
    time_array = time.localtime(start_time)
    return time.strftime("%Y-%m-%d %H:%M:%S",time_array)

if __name__ == '__main__':
    for i in range(1, 1000):
        print("%s,%s,%f,%s,%s") % (get_trans_type(),
        get_trans_source(),
        get_trans_duration(),
        get_trans_code(),
        get_trans_start_time())
