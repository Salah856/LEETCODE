from collections import Counter

class Solution(object):
    def singleNumber(self, nums):
        
        c = Counter(nums)
        
        for k, v in c.items():
            
            if v == 1:
                
                return k
        
