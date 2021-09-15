class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        
        n = sorted(nums)
        l = len(nums)
        
        for i in range(l):
            nums[i] = n.index(nums[i])
        
        return nums    
            
            
