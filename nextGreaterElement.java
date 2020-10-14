class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        
        
        Map<Integer,Integer> map=new HashMap<>();
        for(int i=0;i<nums2.length;i++)
        {
            map.put(nums2[i],i);
        }
        
        int[] res=new int[nums1.length];
        Arrays.fill(res,-1);
        int k=0;
        for(int i=0;i<nums1.length;i++)
        {
            
            int index=map.get(nums1[i]);
            int j=index+1;
            while(j<nums2.length)
            {
                if(nums2[j]>nums1[i])
                {
                    res[k]=nums2[j];
                    break;
                }
                 j++;
            }
           
            k++;
            
            
        }
        
        return res;
        
        
    }
}
