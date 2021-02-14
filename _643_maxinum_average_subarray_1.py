#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 17:18:23 2021

@author: YaoJunyan
"""

#643 maxinum averrage subarray 1

#sliding window
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur = best = sum(nums[:k])
        for i in range(k, len(nums)):
            cur += nums[i] - nums[i-k]
            best = max(best, cur)
        return best / k
    
#time O(n)
#spaceO(1)