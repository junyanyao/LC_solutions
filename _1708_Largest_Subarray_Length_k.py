#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 23:30:54 2021

@author: YaoJunyan
"""
# 1708 Largest Subarray Length K
class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        #find the largest integer in the range[0,n-k]
        max_= 0
        for i in range(0,len(nums)-k+1):
            if nums[i] > nums[max_]:
                max_= i
                
        return nums[max_:max_+k]