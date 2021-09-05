class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
        def count(num):
            ones = 0 
            b = bin(num)[2:]
            for bit in b:
                if bit == '1':
                    ones += 1
                    
            return ones
        
        a = []
        
        for i in range(n + 1):
            
            c = count(i)
            
            a.append(c)
        
        
        return a
            
            
