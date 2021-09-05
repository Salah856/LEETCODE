class Solution {
public:
    bool isPowerOfFour(int n) {
        while(n>=1 && n%4 == 0){
            n = n>>2;
        }
        return (n==1);
    }
};
