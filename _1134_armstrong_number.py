#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 16:10:46 2021

@author: YaoJunyan
"""
# 1134 Armstrong number

class Solution(object):
    def isArmstrong(self, N):
        """
        :type N: int
        :rtype: bool
        """
        l= [int(i) for i in str(N)]
        k= len(l)
        return N == sum([i**k for i in l])
    