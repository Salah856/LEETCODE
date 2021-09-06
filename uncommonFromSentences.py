from collections import Counter

class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        s = s1 + " " + s2
        
        arr = s.split()
        
        items = Counter(arr).items()
        
        res = []
        
        for k, v in items:
            
            if v == 1:
                res.append(k)
                
                
                
        return res        
        
        
