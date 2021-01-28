#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 13:12:36 2021

@author: YaoJunyan
"""
#1672. Richest Customer Wealth
def wealthiest(accounts):
    max_val = 0
    for i in range(len(accounts)):
        if sum(accounts[i]) > max_val:
            max_val = sum(accounts[i])
    return max_val

#Time: O(n)
#Space: O(1)