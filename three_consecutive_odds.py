class Solution(object):
    def threeConsecutiveOdds(self, a):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        for i in range(len(a)-2):
            
            if a[i] % 2 != 0 and a[i+1] % 2 != 0 and a[i+2] % 2 != 0:
                return True 
        
        
        return False
        
