class Solution {
    public int minSwap(int[] nums1, int[] nums2) {
        int[][] dp = new int[nums1.length][2];
        //dp[0][0] = 0; if we do not swap, then nb of swap is 0
        dp[0][1] = 1; // if we swap the first, then nb of swap is 1 
        for (int i=1; i<nums1.length; i++){
            int a1 = nums1[i-1];
            int a2 = nums1[i];
            int b1 = nums2[i-1];
            int b2 = nums2[i];
            dp[i][0] = Integer.MAX_VALUE;
            dp[i][1] = Integer.MAX_VALUE;
            if (a1<a2 && b1 <b2){
                if (a1<b2 && b1<a2){
                    dp[i][0] = Math.min(Math.min(dp[i-1][0], dp[i-1][1]), dp[i][0]);
                    dp[i][1] = Math.min(Math.min(dp[i-1][0]+1,dp[i-1][1]+1), dp[i][1]);
                }else{
                    dp[i][0] = Math.min(dp[i-1][0], dp[i][0]);
                    dp[i][1] = Math.min(dp[i-1][1]+1, dp[i][1]);
                }
            }else{
                dp[i][0] = Math.min(dp[i-1][1], dp[i][0]);
                dp[i][1] = Math.min(dp[i-1][0]+1, dp[i][1]);
            }
           // System.out.print(dp[i][0]+","+dp[i][1]+" ");
        }
        //System.out.println();
        return Math.min(dp[nums1.length-1][0], dp[nums1.length-1][1]);
    }
}
