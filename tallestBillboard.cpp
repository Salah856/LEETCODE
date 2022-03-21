class Solution {
public:
    int tallestBillboard(vector<int>& nums) {
        int sum=accumulate(nums.begin(),nums.end(),0);
        vector<int> dp(sum+1,-1),curr;
        dp[0]=0;
        for(int &el: nums){
            // storing the immediate calculated values
            curr=dp;
            for(int i=0;i<=sum-el;++i){
                // not computed still now
                // so skip it
                if(curr[i] < 0)
                    continue;
                // putting rod into heighest side
                dp[i+el]=max(dp[i+el],curr[i]);
                // putting rod into smallest side
                dp[abs(i-el)]=max(dp[abs(i-el)],curr[i]+min(i,el));
            }
        }
        // we need equal sizes so diff =0 will be my ans
        return dp[0];
    }
    }; 
