#!选择排序
# -*- coding: UTF-8 -*-

import random
import datetime

global val
val = 0

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        global val
        val = val+1
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    print "一共遍历%d次比较" %(val)
    return newArr

def make_list(length):
    last_one = 1
    my_list = range(length)
    for i in range(length):
        last_one = random.randint(1,10000)
        my_list[i] = last_one
    print my_list
    return my_list
    
my_list = make_list(2000)

start = datetime.datetime.now()
print selectionSort(my_list)
end = datetime.datetime.now()
print (end-start)

