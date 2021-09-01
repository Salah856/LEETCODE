class Solution(object):
    def squareIsWhite(self, c):
        """
        :type coordinates: str
        :rtype: bool
        """
        
        letters = "abcdefgh"
        
        
        f = c[0]
        d = int(c[1])
        
        if d % 2 != 0 and (letters.index(f)+1) % 2 != 0:
            return False 
        
        elif d%2 == 0 and (letters.index(f)+1) % 2 == 0:
            return False 
        
        
        else:
            return True
        
