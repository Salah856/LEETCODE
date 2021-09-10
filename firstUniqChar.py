from collections import Counter

class Solution(object):
    def firstUniqChar(self, s):
        
        """
        :type s: str
        :rtype: int
        """
        
        c = Counter(s).items()
        a = []
        
        for k, v in c:
            if v == 1:
                a.append(s.index(k))
        
        
        if len(a) > 0:
            return min(a)
        
        return -1
        
        
