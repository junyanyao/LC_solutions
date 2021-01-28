#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 17:38:34 2021

@author: YaoJunyan
"""
#125 Valid Palindrome
#双指针从两头走到中间

def validPalindrome(s):
    l, r = 0, len(s)-1
    while l< r:
        while l<r and not s[l].lower().isalum():
            l +=1
        while l<r and not s[r].lower().isalnum():
            r -=1
        if s[l].lower().isalnum() != s[r].lower().isalnum():
            return False
        l +=1
        r -=1
    return True