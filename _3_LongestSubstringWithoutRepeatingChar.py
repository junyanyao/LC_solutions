#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 17:01:15 2021

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
