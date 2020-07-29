#!快速排序
# -*- coding: UTF-8 -*-

import random
import datetime

def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

def make_list(length):
    last_one = 1
    my_list = range(length)
    for i in range(length):
        last_one = random.randint(1,10000)
        my_list[i] = last_one
    print "随机生成的数组为：%s\n数组长度为:%d。"%(my_list,length)
    return my_list
    
my_list = make_list(2000)


start = datetime.datetime.now()
print quicksort(my_list)
end = datetime.datetime.now()
print (end-start)


