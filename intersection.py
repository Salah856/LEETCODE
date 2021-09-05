class Solution(object):
    def intersection(self, nums1, nums2):
        
        n1 = set(nums1)
        
        n2 = set(nums2)
        
        return list(n1.intersection(n2))
        
        
