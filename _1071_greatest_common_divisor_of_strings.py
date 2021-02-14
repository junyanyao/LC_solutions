#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 20:47:20 2021

@author: YaoJunyan
"""

#1071 Greatest Commom Divisor of Strings


class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        ans = 0
        if str1 + str2 != str2 + str1:
            return ""
        if len(str1) > len(str2):
            str1 , str2 = str2, str1
            #str 1 now has the shorter  length
        for i in range(len(str1)):
            temp = str1[:i+1]
            print(temp)
            if str2.replace(temp,'')=='' and str1.replace(temp, '')=='':
                ans= i+1
        return str1[:ans]
