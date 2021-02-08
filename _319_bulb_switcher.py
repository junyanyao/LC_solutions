#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 16:31:54 2021

@author: YaoJunyan
"""

#Bulb switcher

class Solution:
    def bulbSwitch(self, n: int) -> int:
        # binary search for the largest int square root
        l, r = 0, n
        ans = 0
        while l <=r:
            mid = (l+r) //2
            if n == mid * mid:
                return mid
            elif n < mid *mid:
                r =  mid -1
            else:
                l =  mid +1
                ans = mid
        return ans
#time olog(n)
#space O(1)

