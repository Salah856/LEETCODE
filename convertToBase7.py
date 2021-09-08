class Solution:
    def convertToBase7(self, num):
        if num == 0:
            return '0'
        
        
        ret = ''
        
        sign = -1 if num < 0 else 1
        
        num = num * sign
        
        while num > 0:
            
            x = num % 7
            
            ret = str(x) + ret
            
            num = num//7
        
        if sign == -1:
            ret = '-' + ret
        
        return ret
