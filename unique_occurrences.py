from collections import Counter

class Solution(object):
    def uniqueOccurrences(self, arr):
        
        c = Counter(arr)
        is_unique = [] 
        
        
        for k, v in c.items():
            
            is_unique.append(v)
            
        
        l = set(is_unique)
        
        return len(l) == len(is_unique)
        
        
