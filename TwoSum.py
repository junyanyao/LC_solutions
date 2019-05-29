#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 21:42:31 2019

@author: YaoJunyan
"""

##Two Sum

#Solution 1 (Brute Force):
#This is the simplest way to understand
# basically you can consider it as X+Y =Z, Now we know Z is fixed. Just need to iterate through lists to find X and Y
#However this is very inefficient
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] +nums[j] == target and i !=j:
                return [i, j]

#test case: nums = [2,7,11,15], target = 9

nums = [2,7,11,15]
target =9

print(twoSum(nums, target))
# [0,1]



#Solution 2:
# slightly better than Solution1 because this solution can only require one iteration
#while we iterate and inserting elements into the table, we also look back to check if current element's complement already exists in the table.


def twoSum2(nums, target):
    dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement not in dict:
            dict[num] = i
        else:
            return [dict[complement], i]
print(twoSum2(nums, target))