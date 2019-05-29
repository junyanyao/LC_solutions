#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 22:13:24 2019

@author: YaoJunyan
"""

#Valid Parentheses


# this question is better to use stack 

def isValid(s):
    lookup = {'(':')', '{' :'}', '[':']'}
    stack = []
    for c in s:
        if c in lookup:
            stack.append(c)
        elif len(stack) ==0 or lookup(stack.pop()) != c:
            return False
        
    return len(stack) ==0