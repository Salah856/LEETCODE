class Solution:
    def repeatedSubstringPattern(self, s):
        length = len(s)
        
        if length == 1:
            return False
        
        for i in range(1, length + 1):
            
            if length % i == 0 and length / i != 1:
                
                temp_str = s[0:i] * int(length / i)
                
                if temp_str == s:
                    return True
        
        return False
