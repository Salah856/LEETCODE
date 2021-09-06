class Solution(object):
    def maxScore(self, s):
        
        res = -float('inf')
        
        for i in range(1,len(s)):
            temp = s[:i].count('0') + s[i:].count('1')
            res = max(res, temp)
       
        return res
