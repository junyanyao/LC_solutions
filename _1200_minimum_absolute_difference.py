#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 16:26:29 2021

@author: YaoJunyan
"""

#1200. Minimum Absolute Difference
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans = []
        min_d = arr[1]- arr[0]
        for i in range(len(arr)-1):
            min_d = min(min_d, arr[i+1]- arr[i])
        for i in range(len(arr)-1):
            d = arr[i+1]- arr[i]
            if d == min_d:
                ans.append([arr[i],arr[i+1]])
        return ans
#Time: O(n)