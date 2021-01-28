#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 12:43:19 2021

@author: YaoJunyan
"""

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n= len(nums)
        return max(nums[0]*nums[1]*nums[n-1], nums[n-1]*nums[n-2]*nums[n-3])
    
    
    


#Time complexity : O\big(n\log n\big)O(nlogn). Sorting the numsnums array takes n\log nnlogn time.

#Space complexity : O(\log n)O(logn). Sorting takes O(\log n)O(logn) space.

#Single Scan

