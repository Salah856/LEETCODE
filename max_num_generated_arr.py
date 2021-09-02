class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        
        nums, i = [0, 1], 1

        while len(nums) < n + 1:
            
            nums += [nums[i]]
            nums += [nums[i] + nums[i + 1]]
            
            i += 1

        return max(nums[:-1]) if n % 2 == 0 else max(nums)
