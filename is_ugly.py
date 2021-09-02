class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<1: return False
        
        while n%2==0: n /= 2 #if n is still divisible by 2, divide it by 2 until it cannot.
        while n%3==0: n /= 3
        while n%5==0: n /= 5
            
        return n==1
        
