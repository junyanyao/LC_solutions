#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 22:21:38 2021

@author: YaoJunyan
"""
#Assign Cookie

#two pointer

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        ans = 0
        j = 0
        i = 0
        while i<len(g) and j < len(s):
            if s[j] >=g[i]:
                ans +=1
                i+=1
                j+=1
            else:
                j+=1
        return ans