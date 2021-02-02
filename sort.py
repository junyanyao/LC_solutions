#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 20:29:41 2021

@author: YaoJunyan
"""
import collections

l = [2, 2, 0, 0, 1, 1, 0, 2, 3 ] 
def find(l):
    d = collections.defaultdict(int)
    for i in l:
        d[i] +=1
        
    return d

        

def buble_sort(x):
    for i in range(len(x)):
        for j in range(len(x)-i-1):
            if x[j] > x[j+1]:
                x[j+1], x[j] = x[j], x[j+1]
    return x
from random import randint

def quicksort(array):
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    # Select your `pivot` element randomly
    pivot = array[randint(0, len(array) - 1)]

    for item in array:
        # Elements that are smaller than the `pivot` go to
        # the `low` list. Elements that are larger than
        # `pivot` go to the `high` list. Elements that are
        # equal to `pivot` go to the `same` list.
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    # The final result combines the sorted `low` list
    # with the `same` list and the sorted `high` list
    return quicksort(low) + same + quicksort(high)

def move(l):
    n= sum([i ==0 for i in l])
    pre = [0]* n
    ans = []
    for p in l:
        if p !=0:
            ans.append(p)
    return pre +ans