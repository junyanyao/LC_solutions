#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 16:45:08 2021

@author: YaoJunyan
"""

#561 array partition 1

#find the pairing pattern
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for idx, val in enumerate(nums):
            if idx %2 ==0:
                ans += val
        return ans
#time Nlog(N)


#sort takes Nlog(N) time. we iterate over the array only once

#space is O(n) sort in python takes O(n) for space
