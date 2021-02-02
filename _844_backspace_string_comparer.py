#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 22:38:51 2021

@author: YaoJunyan
"""

#844 Backspace String Compare
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        
        s=[]
        t=[]
        for i in range(len(S)):
            if S[i] != '#':
                s.append(S[i])
            elif len(s) !=0:
                s.pop()
        for j in range(len(T)):
            if T[j] != '#':
                t.append(T[j])
            elif len(t) >0:
                t.pop()
        return t==s
    
#Time Complexity: O(M + N)O(M+N), where M, NM,N are the lengths of S and T respectively.

#Space Complexity: O(M + N)O(M+N).

#use two pointer can achieve O(1) space
