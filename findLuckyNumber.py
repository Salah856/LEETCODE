from collections import Counter

class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        c = Counter(arr)
        
        r = [] 
        
        for k, v in c.items():
            if k == v:
                r.append(k)
            
        
        return max(r) if len(r) >= 1 else -1 
        
        
