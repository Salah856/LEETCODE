def merge(nums1, nums2): 
        
        i = 0
        
        while i <= n - 1:
            j = m - 1
            
            while j > -1 and nums1[j] > nums2[i]:
                j -= 1
            
            k = m - 1
            while k > j:
                nums1[k + 1] = nums1[k]
                k -= 1
                
            
            nums1[j + 1] = nums2[i]

            i += 1
            m += 1
