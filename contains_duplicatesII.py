class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        
        hashtable = dict()
        
        for inx, i in enumerate(nums):
            
            if i in hashtable and abs(inx - hashtable[i]) <= k:
                return True
            
            hashtable[i] = inx
        
        return False
            
        
        
