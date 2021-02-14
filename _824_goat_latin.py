#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 21:14:29 2021

@author: YaoJunyan
"""

#824 Goat Latin


class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        ans = []
        vowels = 'aeiouAEIOU'
        words = S.split(' ')
        for i,w in enumerate(words):
            if w[0] in vowels:
                w += 'ma'
            else:
                w= w[1:]+w[0] + 'ma'
            w+='a'*(i+1) 
            ans.append(w)
        return ' '.join(ans)
            