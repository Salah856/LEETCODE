class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        numsCovered = set(i for start, end in ranges for i in range(start, end+1))
        
        for i in range(left, right+1):
            if i not in numsCovered:
                return False
        
        return True
        
        
