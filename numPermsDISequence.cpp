class Solution {
public:
    int dp[203][203];
    int mod=1e9+7;
    int solve(int index , string& s, vector<int> & visited , int prev){
        if(index==s.size()) return 1;
        if(dp[index][prev]!=-1) return dp[index][prev];
        int n=s.size();
        long long temp=0;
        if(s[index]=='D'){
            //0 to prev-1
            for(int i=0;i<=prev-1;i++){
                if(visited[i]==0){
                    visited[i]=1;
                    temp=(temp%mod+(long long)solve(index+1,s,visited,i)%mod)%mod;

                    visited[i]=0;
                }
            }
        }else {
            //prev+1 to n
            for(int i=prev+1;i<=n;i++){
                if(visited[i]==0){
                    visited[i]=1;
                    temp=(temp%mod+(long long)solve(index+1,s,visited,i)%mod)%mod;
                    visited[i]=0;
                }
            }
        }
        return dp[index][prev]=temp;
    }
    int numPermsDISequence(string s) {
        memset(dp,-1,sizeof dp);
        int n=s.size();
        vector<int> visited(n+1,0);
        int count=0;
        for(int i=0;i<=n;i++){
            visited[i]=1;
            count= (count%mod+(long long)solve(0,s,visited,i)%mod)%mod;
            visited[i]=0;
        }
        return count;
    }
};
