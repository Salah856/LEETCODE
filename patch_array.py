class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        
        prevNum=0
        patches=0
        i=0
        
        while i<len(nums):
            num=nums[i]
            
            if(prevNum>=n): return patches
            
            if(num<=prevNum+1):
                prevNum=prevNum+num
                i+=1
            
            else:
                patches+=1
                prevNum=prevNum+prevNum+1
        
        if(prevNum<n):
            
            while prevNum<n:
                patches+=1
                prevNum+=prevNum+1
        
        return patches
        
