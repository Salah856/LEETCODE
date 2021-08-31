class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
		# two pointers technique
        
        start = 0
        end = len(nums)-1
        
        while start <= end:
            
            if nums[start] + nums[end] == target:
                return [start+1, end+1]
            
            elif nums[start] + nums[end] < target:
                start += 1
            
            else:
                end -= 1
				
		# using hashmap (dict).
		
        h = {}
        
        for i,j in enumerate(nums):
            k = target - j
            if k not in h:
                h[j] = i + 1
            else:
                return [h[k], i+1]
            
            
