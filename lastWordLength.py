class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split()
        lastWord = words[-1]
        
        return len(lastWord)
        
        
