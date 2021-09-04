class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        charMap = {}
        maxDiff = -1
        
        for i, char in enumerate(s):
            if char not in charMap:
                charMap[char] = i
            elif i - charMap[char] - 1 > maxDiff:
                maxDiff = i - charMap[char] - 1
                
        return maxDiff
