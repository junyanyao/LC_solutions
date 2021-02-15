#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 15:13:00 2021

@author: YaoJunyan
"""

#438 Find all Anagrams


#Sliding window wth array

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pcount = [0]*26
        scount = [0] *26
        len_p = len(p)
        len_s = len(s)
        res = []
        for ch in p:
            pcount[ord(ch)- ord('a')] +=1
            
        for i in range(len(s)):
            scount[ord(s[i]) - ord('a')] +=1
            if i >=len_p:
                scount[ord(s[i-len_p])- ord('a')] -=1
            if pcount == scount:
                res.append(i-len_p+1)
        return res
#Time O(n+m)
#space:O(1)

#固定窗口tle


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        def helper(s1, s2):
            return collections.Counter(s1) == collections.Counter(s2)
        
        j= len(p)
        ans = []
        for i in range(0,len(s)-j+1):
            print(s[i:j])
            if helper(s[i:j], p):
                ans.append(i)
            j+=1
        return ans
            