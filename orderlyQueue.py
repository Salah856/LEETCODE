class Solution:
    
    def orderlyQueue(self, s, k):
        l = len(s)
        
        if k == 1: 
            return min(s[i:] + s[:i] for i in range(l))
        
        return "".join(sorted(s))
        
