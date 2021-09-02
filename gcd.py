class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        mn = min(nums)
        
        mx = max(nums)
        
        def gcd(x, y):  
            if (y == 0): # it divide every number  
                return x  # return x  
            else:  
                return gcd(y, x % y)  
        
        return gcd(mn, mx)
        
