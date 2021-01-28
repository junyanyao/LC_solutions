#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 12:25:28 2021

@author: YaoJunyan
"""
# Find the highest Altitude

class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        #[-5,1,5,0,-7]
        #[0, 0-5, 0-5+1, 0-5+1+5,0-5+1+5+0,0-5+1+5+0-7 ]
        altitudes = [0]
        max_ = 0
        val = 0
        for i in range(len(gain)):
            val = altitudes[-1] + gain[i]
            altitudes.append(val)
            max_= max(val, max_)
        return max_
#Time: O(n)
#Space: O(1)

class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        #[-5,1,5,0,-7]
        #[0, 0-5, 0-5+1, 0-5+1+5,0-5+1+5+0,0-5+1+5+0-7 ]
        cur = 0
        best = 0
        for i in gain:
            cur += i 
            if cur > best:
                best = cur
        return best