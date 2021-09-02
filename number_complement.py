class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        n_digit = 0
        num_copy = num
        
        while num_copy >= 2:
            num_copy = num_copy/2
            n_digit = n_digit + 1
        
        return 2**(n_digit + 1) - 1 - num
