class Solution(object):
    def check(self, nums):
        
        ans = sorted(nums)
        nums = nums + nums
        
        
        for i in range(0, len(nums) // 2):
            
            if nums[i : len(nums) // 2 + i] == ans:
                return True
        
        
        return False
        
