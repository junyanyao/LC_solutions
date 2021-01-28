#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 15:46:02 2021

@author: YaoJunyan
"""


class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        s = sum(x for x in A if x %2 ==0)
        ans = []
        for x,k in queries:
            if A[k] %2 ==0:
                s-= A[k]
            A[k] +=x
            if A[k] %2 ==0:
                s += A[k]
            ans.append(s)
                
        return ans
            
#Time Complexity: O(N+Q)O(N+Q), where N is the length of A and Q is the number of queries.

#Space Complexity: O(Q), though we only allocate O(1) additional space.