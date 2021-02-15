
#Time Limit exceed
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        ans = False
        def helper(s,t):
            return collections.Counter(s) ==collections.Counter(t)
        j=len(s1)
        for i in range(len(s2)-j+1):
            if helper(s2[i:j], s1):
                ans = True
            j +=1
        return ans
#Time O(n+m)
#Space O(1)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        A= [ord(i)- ord('a') for i in s1]
        B = [ord(i)- ord('a') for i in s2]
        target = [0] *26
        for ch in A:
            target[ch] +=1
        ans = False
        maps= [0] *26  
        for i in range(len(B)):
            maps[B[i]] +=1
            if i >= len(A):
                maps[B[i- len(A)]] -=1
            if maps == target:
                ans = True
        return ans

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1count = [0] *26
        s2count = [0] *26
        ans = False
        for ch in s1:
            s1count[ord(ch) - ord('a')] +=1
        len_1= len(s1)
        len_2 = len(s2)
        for i in range(len_2):
            s2count[ord(s2[i])- ord('a')] +=1
            #add values from right
            if i >= len_1:
                #固定窗口i- len(s1)
                s2count[ord(s2[i-len_1])- ord('a')] -=1
                #substract values from left
            if s1count == s2count:
                #if condition hold:
                ans = True
        return ans