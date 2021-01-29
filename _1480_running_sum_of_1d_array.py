#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 16:00:39 2021

@author: YaoJunyan
"""
# 1480 Running Sum of 1d Array
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        cur = 0
        for i in range(len(nums)):
            cur += nums[i]
            nums[i]= cur
        return nums
    
#O(n) Time Complexity and O(1) Space Complexity