class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary = '{0:08b}'.format(n)
        
        c = 0
        
        for i in binary: 
            if i == '1':
                c+=1
                
          
        return c
        
        
