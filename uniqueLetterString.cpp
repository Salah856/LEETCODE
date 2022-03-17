class Solution {
public:
    int uniqueLetterString(string s) {
        vector<int> v[26];
        int n=s.length();
        for(int i=0; i<26; i++) v[i].push_back(-1);
        for(int i=0; i<n; i++) {
            v[s[i]-'A'].push_back(i);
        }
        int res=0;
        for(int i=0; i<26; i++) {
            v[i].push_back(n);
            for(int j=1; j<v[i].size()-1; j++) {
                res+=(v[i][j]-v[i][j-1])*(v[i][j+1]-v[i][j]);
            }
        }
        return res;
    }
};
