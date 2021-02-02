#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 22:02:16 2021

@author: YaoJunyan
"""

# 3 longest substring without repeating characters

#解法1:单指针： window是滑窗内字符的集合，初始化为空。从前向后移动滑窗，同时更新当前子串长度cur_len和最长子串长度max_len。当滑窗右端移动到字符ch：
#如果ch已存在window中，那么从滑窗的左端起删除字符，直到删除ch。每删除一个字符cur_len减1。
#将ch添加到window中，cur_len加1。
#更新最长子串长度max_len。
#返回max_len。



def lengthOfLongestSubstring(s):
    if s =='':
        return 0
    window = set()
    left = 0
    cur_len= 0
    max_len = 0
    for ch in s:
        while ch not in window:
            window.remove(s[left])
            cur_len -=1
        window.add(ch)
        cur_len +=1
        max_len= max(max_len, cur_len)
    return max_len

# 解法2:
#双指针滑动窗口的经典写法。右指针不断往右移，移动到不能往右移动为止(具体条件根据题目而定)。当右指针到最右边以后，开始挪动左指针，释放窗口左边界

#滑动窗口的右边界不断的右移，只要没有重复的字符，就持续向右扩大窗口边界。一旦出现了重复字符，就需要缩小左边界，直到重复的字符移出了左边界，然后继续移动滑动窗口的右边界。以此类推，每次移动需要计算当前长度，并判断是否需要更新最大长度，最终最大的值就是题目中的所求。


def lengthOfLongestSubstring(s):
    start = 0
    end = 0
    store = {}
    
    max_len =0
    while end < len(s) and start <= end:
        if s[end] in store:
            store.pop(s[start])
            start +=1
        else:
            store[s[end]]==True
            end +=1
            max_len = max(len(store), max_len)
    return max_len


# 11 Container with most water
#这一题也是对撞指针的思路。首尾分别 2 个指针，每次移动以后都分别判断长宽的乘积是否最大。
#O(n)
def maxArea(height):
    l,r = 0, len(height)-1
    max_area = 0
    while l < r:
        width = r- l
        high = 0
        if height[l] > height[r]:
            high = height[r]
            r -=1
        else:
            high = height[l]
            l +=1
        area = width * high
        max_area = max(max_area, area)
    return max_area
    

#125 Valid Palindrome
#双指针从两头走到中间

def validPalindrome(s):
    l, r = 0, len(s)-1
    while l< r:
        while l<r and not s[l].lower().isalum():
            l +=1
        while l<r and not s[r].lower().isalnum():
            r -=1
        if s[l].lower().isalnum() != s[r].lower().isalnum():
            return False
        l +=1
        r -=1
    return True

#680 Valid Palindrome 2

# 双指针算法。从两头走到中间，发现第一对不一样的字符之后，要么删左边的，要么删右边的。


def validPalindrome2(s):
    def isValid(s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left +=1
            right -=1
        return True
    l, r = 0, len(s)-1
    while l < r:
        if s[l] != s[r]:
            return isValid(s, l, r-1) or isValid(s, l+1, r)
        l +=1
        r -=1
    return True

        
# 349 intersections of two arrays

#把数组一的每个数字都存进字典中，然后在数组二中依次判断字典中是否存在，如果存在，在字典中删除它(因为输出要求只输出一次)。

def intersection(num1, num2):
    res = []
    d = {}
    for i in num1:
        d[i] = True
    for j in num2:
        if j in d:
            del d[j]
            res.append(j)
    return res
            
# 350 Intersections of two arrays 2    
#这一题还是延续第 349 题的思路。把数组一中的数字都放进字典中，另外字典的 key 是数组中的数字，value 是这个数字出现的次数。
#在扫描数组二的时候，每取出一个存在的数组，把字典中的 value 减一。如果 value 是 0 代表不存在这个数字。÷÷Ωx
def intersection2(num1, num2):
    res = []
    d = defaultdict(int)
    for i in num1:
        d[i] +=1
    for j in num2:
        if d[j] >0:
            res.append(j)
            d[j] -=1
    return res

#find all anagrams in a string

#use a hashtable to represent p and then sliding window

def anagrams(s,p):
    d= {}
    l,r =0,0
    cnt = 0
    res = []
    for i in p:
        if i not in d:
            d[i] =1
        else:
            d[i] +=1
    while r < len(s):
        if d[s[r]] >0:
            cnt -=1
        d[s[r]] -=1
        r+=1
        if cnt ==0:
            res.append(l)
        if r-l == len(p):
            if d[s[l]] >=0:
                cnt +=1
            d[s[l]] +=1
            l+=1
    return res
    

area = 0
x =[0,0.2,0.33,0.43,0.63,0.66,1]
y= [0,0.25,0.25,0.5,0.5,1,1]
for i in range(len(x)-1):
    area += (y[i+1]+y[i])*(x[i+1]-x[i]) /2


def solution



df = df.dropna(how='any',axis=0) 





