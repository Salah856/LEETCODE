class Solution:
    def minMoves(self, nums: List[int]) -> int:
        
        n = len(nums)
        min_nums = min(nums)
        
        return sum(nums) - (n * min_nums)
