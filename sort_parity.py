class Solution:
    
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        
        even, odd = [], []
        
        for num in nums:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        
        output = []
        j = 0
        
        for i in range(len(odd)):
            
            output.append(even[j])
            output.append(odd[i])
            
            j += 1
        
        return output
    
    
