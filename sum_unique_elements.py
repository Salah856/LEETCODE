from collections import Counter

class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        s = 0 
        
        c = Counter(nums)
        
        for k, v in c.items():
            
            if v == 1:
                s += k 
                
        
        return s
        
