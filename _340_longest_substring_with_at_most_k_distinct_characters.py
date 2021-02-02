#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 18:03:41 2021

@author: YaoJunyan
"""

#340 Longest Substring with at most K distinct Characters

#Sliding window using Hashmap

#two pointers in the same direction

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        maps = defaultdict(int)
        distinct = 0
        length = []
        j = 0
        for i in range(len(s)):
            maps[s[i]] +=1
            if maps[s[i]] ==1:
                distinct +=1
            while distinct > k:
                maps[s[j]] -=1
                if maps[s[j]] ==0:
                    distinct -=1
                j +=1
            length.append(i-j+1)
        return max(length)
    


class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        window = []
        cur = 0
        max_= 0
        for i in range(len(s)):
            window.append(s[i])
            cur +=1
            while len(set(window)) >k:
                window.pop(0)
                cur -=1
            max_=  max(max_, cur)
        return max_