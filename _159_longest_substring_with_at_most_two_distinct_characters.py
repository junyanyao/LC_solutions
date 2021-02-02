#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 17:45:32 2021

@author: YaoJunyan
"""

#159 Longest substring with at most two distinct characters


#Sliding window
#two pointers in same direction
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        cur = 0
        max_ = 0

        window = list()
        for i in range(len(s)):
            window.append(s[i])
            cur +=1
            while len(set(window)) >2:
                window.pop(0)
                cur -=1
            max_= max(max_, cur)
            
        return max_
    
#or hashmap way
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        #sliding window
        if s=='':
            return 0
        j = 0
        distinct =0
        length = []
        maps = defaultdict(int)
        for i in range(len(s)):
            maps[s[i]] +=1
            if maps[s[i]] ==1:
                distinct +=1
            while distinct > 2:
                maps[s[j]] -=1
                if maps[s[j]]==0:
                    distinct -=1
                j +=1
            length.append(i -j +1 )
        return max(length)
#Two pointers but writing in different way

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        #sliding window
        if s=='':
            return 0
        j = 0
        distinct =0
        length = []
        i = 0
        maps = defaultdict(int)
        while i < len(s):
            maps[s[i]] +=1
            if maps[s[i]] == 1:
                distinct +=1
            if distinct >2:
                maps[s[j]] -=1
                if maps[s[j]] ==0:
                    distinct -=1
                j +=1
            length.append(i -j +1)
            i+=1
        return max(length)

