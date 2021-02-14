#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 21:23:07 2021

@author: YaoJunyan
"""

#1436 Destination City
class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        b= [i[0] for i in paths]
        print(b)
        for i in range(len(paths)):
            if paths[i][1] not in b:
                return paths[i][1]