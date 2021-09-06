class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return ""
        
        chars = set(s)
        
        for i, c in enumerate(s):
            if c.upper() not in chars or c.lower() not in chars:
                s1 = self.longestNiceSubstring(s[:i])
                s2 = self.longestNiceSubstring(s[i+1:])
                return s1 if len(s1) >= len(s2) else s2
            
        return s
        
