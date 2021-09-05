class Solution(object):
    def generateTheString(self, n):
        
        alpha = "abcdefghijklmnopqrstuvwxyz"
        
        if n == 1: 
            return "a"
        
        if n == 0:
            return ""
        
        if n==2:
            return alpha[:2]
        
        if n > 26 and n % 2 != 0:
            return "a" * n 
        
        
        if n > 0 and n % 2 != 0: 
            return alpha[:n]
        
        
        
        if n > 0 and n % 2 == 0:
            
            odd1 = n / 2 - 1
            
            if odd1 % 2 == 0:
                odd1 -= 1
            
            odd2 = n - odd1 
            
            return "a" * odd1 + "b" * odd2
        
       
