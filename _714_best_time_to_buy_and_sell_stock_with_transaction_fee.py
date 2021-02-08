#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 23:20:39 2021

@author: YaoJunyan
"""

#714 best time to buy and sell stock with transaction fee

#dynamtic programing
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        cash = 0
        hold = -prices[0]
        for i in range(1, len(prices)):
            cash = max(cash, hold + prices[i]-fee)
            hold = max(hold, cash - prices[i])
        return cash
        