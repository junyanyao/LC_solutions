#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 17:22:00 2021

@author: YaoJunyan
"""

# 11 Container with most water
#这一题也是对撞指针的思路。首尾分别 2 个指针，每次移动以后都分别判断长宽的乘积是否最大。
#O(n)
def maxArea(height):
    l,r = 0, len(height)-1
    max_area = 0
    while l < r:
        width = r- l
        high = 0
        if height[l] > height[r]:
            high = height[r]
            r -=1
        else:
            high = height[l]
            l +=1
        area = width * high
        max_area = max(max_area, area)
    return max_area
    