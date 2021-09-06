class Solution:
    def canBeIncreasing(self, nums):
        dip = -1
        for i in range(1, len(nums)):
            if nums[i-1] >= nums[i]:
                # Record the index where we "dip", where we violate the strictly increasing order property
                if dip == -1:
                    dip = i
                else:
                    return False
        
        if dip == -1:
            return True
        
        # If the dip happened at the end of nums, we could just cut it off and the list would become strictly
        # increasing; Or if cutting out nums[dip] results in nums[dip-1] < nums[dip+1], that also works
        if dip == len(nums) - 1 or nums[dip-1] < nums[dip+1]:
            return True
        
        # If the dip happened at the second element (index = 1), we could just cut off the higher element at
        # index == 0; Or if cutting out nums[dip-1] results in nums[dip-2] < nums[dip], that also works
        if dip == 1 or nums[dip-2] < nums[dip]:
            return True
        
        return False
