class Solution(object):
    def dominantIndex(self, nums):
        
        v = max(nums)
        i = nums.index(v)
        
        for n in nums:
            if n * 2 > v and n != v:
                i = -1 
        
        return i
    
