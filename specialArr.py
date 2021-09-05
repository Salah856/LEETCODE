class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        
        for i in range(len(nums) + 1):
            
            index = self.binarySearch(nums, i)
            
            if len(nums) - index == i:
                return i
        
        return -1
    
    
    def binarySearch(self, nums, val):
        low, high = 0, len(nums)
        
        while low < high:
            mid = low +  (high - low) // 2
            
            if nums[mid] >= val:
                high = mid
            
            else:
                low = mid + 1
        
        
        return low
        
        
        
