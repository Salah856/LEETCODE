class Solution(object):
    def isPowerOfTwo(self, n):
        
        if n == 1:
            return True
        
        x = 2
        
        while x <= n:
            
            if x == n:
                return True
            
            else:
                x *= 2
        
        return False
        
        
        
