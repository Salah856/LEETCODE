class Solution {
    public int distanceBetweenBusStops(int[] distance, int start, int destination) {
        int beg = 0, mid = 0, end = 0, sum = 0;
        for (int i = 0; i < distance.length; i++) {
            if (i == start) {
                beg = sum;
            } else if (i == destination) {
                end = sum;
            }
            sum += distance[i];
        }
        if (start == destination) return 0;
        return beg < end ? Math.min(end-beg, beg+(sum-end)) : Math.min(beg-end, end+(sum-beg));
    }
}
