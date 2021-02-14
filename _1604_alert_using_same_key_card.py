#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 15:34:44 2021

@author: YaoJunyan
"""


#1604 Alert using same key-card three or more times in one hour period
class Solution(object):
    def alertNames(self, keyName, keyTime):
        """
        :type keyName: List[str]
        :type keyTime: List[str]
        :rtype: List[str]
        """
        result = []
        def timetoint(time):
            h, m = time.split(':')
            return int(h) * 60 +  int(m)
        maps = defaultdict(list)
        for name, time in zip(keyName, keyTime):
            maps[name].append(timetoint(time))
        print(maps)
        for idx, val in maps.items():
            val.sort()
            for i in range(2, len(val)):
                if val[i]- val[i-2] <=60:
                    result.append(idx)
                    break
        result.sort()
        return result