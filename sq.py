class Solution(object):
    def sortedSquares(self, nums):
        
        sq = []
        
        for num in nums:
            sq.append(num * num)
            
        
        sq.sort()
        
        return sq
        
        
