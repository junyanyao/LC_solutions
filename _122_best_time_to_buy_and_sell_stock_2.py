#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 22:43:27 2021

@author: YaoJunyan
"""


#122 best time to buy and sell stock 2

#同向双指针
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        cur = 0
        left, right = 0,1
        while right < len(prices):
            if prices[right]> prices[left]:
                cur= prices[right] - prices[left]
                ans += cur
            right +=1
            left +=1
        return ans
    
#O(n) and O(1)