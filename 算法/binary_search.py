#!二分查找
#-*- coding:UTF-8 -*-

import random

def binary_search(list, item):
    low = 0
    high = len(list)-1
    #print 'low:%d,high:%d' %( low,high )
    while low <= high:
        mid = (low + high)/2
        guess = list[mid]
        print  "得到中间元素是：%d" % (guess)
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

def make_list(length):
    last_one = 1
    my_list = range(length)
    for i in range(length):
        last_one = last_one + random.randint(1,3)
        my_list[i] = last_one
    print my_list
    return my_list
    
#my_list = [1, 3, 5, 7, 9, 11, 12, 13, 15, 16, 18, 20, 25, 32]
my_list = make_list(128)

print binary_search(my_list, 15)
