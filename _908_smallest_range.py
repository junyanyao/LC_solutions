#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 18:05:39 2021

@author: YaoJunyan
"""

#908. Smallest Range I
class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        return max(0,(max(A)- K)- (min(A)+K))
#Time Complexity: O(N), where NN is the length of A.

#Space Complexity: O(1).