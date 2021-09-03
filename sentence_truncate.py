class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
        ss = s.split(' ')
        t = ss[:k]
        
        return " ".join(t)
        
