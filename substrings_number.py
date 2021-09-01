class Solution(object):
    def numOfStrings(self, patterns, word):
        
        c = 0 
        
        for pattern in patterns:
            if pattern in word:
                c += 1
       
        
        return c
