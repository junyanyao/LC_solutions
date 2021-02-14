#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 15:07:28 2021

@author: YaoJunyan
"""

#132 pattern:
    
#O(n^3)
#Space complexity : O(1)O(1). Constant extra space is used.
class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if nums[i]<nums[k]<nums[j]:
                        return True
        return False

#O(n^2)
#Space complexity : O(1)O(1). Constant extra space is used.
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        min_i = inf
        for j in range(len(nums)-1):
            min_i = min(min_i, nums[j])
            for k in range(j+1, len(nums)):
                if min_i< nums[k]<nums[j]:
                    return True
        return False
    
#这一题算是单调栈的经典解法，可以考虑从数组末尾开始往前扫，维护一个递减序列

#https://leetcode-cn.com/problems/132-pattern/solution/zhan-jie-fa-chao-xiang-xi-ti-jie-by-siyy/
class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <2:
            return False
        m1 = [nums[0]]
        for i in range(1,len(nums)):
            m1.append(min(m1[-1], nums[i]))
        stack = []
        for i in range(len(nums)-1,-1,-1):
            #print(stack)
            if nums[i]>m1[i]:
                while stack and m1[i] >= stack[-1]:
                    stack.pop()
                if stack and nums[i] > stack[-1]:
                    return True
                stack.append(nums[i])
        return False