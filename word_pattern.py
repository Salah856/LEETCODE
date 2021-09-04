class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        
        s = s.split()
        
        if len(pattern) != len(s):
            return False
        
        maps = {}
        rmaps = {}
        
        for i in range(len(pattern)):
            
            if pattern[i] in maps:
                if maps[pattern[i]] != s[i]:
                    return False
            
            if s[i] in rmaps:
                if rmaps[s[i]] != pattern[i]:
                    return False
            
            maps[pattern[i]] = s[i]
            
            rmaps[s[i]] = pattern[i]
        
        return True
        
        
        
