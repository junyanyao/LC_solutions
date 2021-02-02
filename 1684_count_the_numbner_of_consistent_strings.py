#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 18:09:24 2021

@author: YaoJunyan
"""
class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        res = 0
        for word in words:
            if all([True if i in allowed else False for i in word]):
                res +=1
        return res
    
class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        res = 0
        for word in words:
            res +=1
            for i in word:
                if i not in allowed:
                    res -=1
                    break
        return res