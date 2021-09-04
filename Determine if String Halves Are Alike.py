class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        half = len(s) / 2
        
        a = s[:half]
        b = s[half:]
        
        a_v = b_v = 0 
        
        for i in range(len(a)):
            if a[i] in vowels:
                a_v += 1
                
            if b[i] in vowels:
                b_v += 1
        
        return a_v == b_v 
        
