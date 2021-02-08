#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 16:14:15 2021

@author: YaoJunyan
"""



#441 arrange coins

#this is a binary search problem

#find the biggest integer that k*(k+1) /2 <=n

class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 0, n
        cur = 0
        while l<=r:
            mid = (l+r) //2
            cur = mid *(mid +1) /2
            if cur ==n:
                return mid
            elif n< cur:
                r= mid -1
            else:
                l = mid+1
        return r
#time : Ologn
#space: O(1)


#or just math questions

#time: O(1)
#space:O(1)
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return (int)((2 * n + 0.25)**0.5 - 0.5)
    
    