#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 00:02:15 2021

@author: YaoJunyan
"""

#1704 Determine if String halves are alike


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        v = ['a','e','i','o','u','A','E','I','O','U']
        n=  len(s)
        l= 0
        r = 0
        for i in s[0:n//2]:
            if i in v:
                l +=1
        for j in s[n//2:n]:
            if j in v:
                r +=1
        return r==l
        #Time: O(n)
        #Space: O(n)