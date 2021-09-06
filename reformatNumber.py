class Solution:
    def reformatNumber(self, number):
        
        nums = [n for n in number if n.isdigit()]
        
        
        formatedNum = []
        
        i = 0
        
        while i < len(nums) - 4:
            
            formatedNum.extend(nums[i:i+3] + ['-'])
            
            i += 3
        
        remainder = len(nums) - i
        
        if remainder == 4:
            formatedNum.extend(nums[i : i + 2] + ['-'] + nums[i + 2 : ])
        
        elif remainder > 1:
            formatedNum.extend(nums[i : ])
        
        
        
        return ''.join(formatedNum)
    
    
