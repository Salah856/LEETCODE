class Solution:
    def maxRepeating(self, sequence, word):
        
        if len(sequence) < len(word):
            return 0
        
        k = 0
        
        while word * (k+1) in sequence:
            k += 1
        
        return k
            
            
        
