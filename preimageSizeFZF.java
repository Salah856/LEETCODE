class Solution {
    public int preimageSizeFZF(int k) {
        long left = 0;
        long right = 5L * (k + 1);
        while (left < right - 1) {
            long mid = left + (right - left) / 2;
            int cnt = countZeros(mid);
            if (cnt == k) {
                return 5;
            } else if (cnt < k) {
                left = mid;
            } else {
                right = mid;
            }
        }
        
        return countZeros(left) == k || countZeros(right) == k ? 5 : 0;
    }
    
    private int countZeros(long n) {
        int rst = 0;
        while (n > 0) {
            rst += n / 5;
            n /= 5;
        }
        return rst;
    }
}
