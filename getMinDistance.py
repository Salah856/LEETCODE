class Solution(object):
    def getMinDistance(self, nums, target, start):
        
        midx = 100000000000000000000000000000000000000000000
        
        for i, num in enumerate(nums):
            
            if num == target:
                
                if abs(i - start) < midx:
                    midx = abs(i - start)
        
        
        return midx 
        
        
        
