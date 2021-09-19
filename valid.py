class Solution:
    def isValid(self, s: str) -> bool:
        
        while len(s) > 0:
            
            last_len = len(s)
            
            s = s.replace('abc', '')
            
            if len(s) == last_len:
                return False
        
        return True
    
    
    
