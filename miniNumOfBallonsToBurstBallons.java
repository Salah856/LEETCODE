class Solution {
    public int findMinArrowShots(int[][] points) {
        
        if(points == null || points.length == 0)
            return 0;
        
        Arrays.sort(points, (a, b) -> Integer.compare(a[0], b[0]));
        int i = 1, count = 1, curr[] = points[0];
        
        while(i < points.length){
            while(i < points.length && points[i][0] <= curr[1])
                curr[1]  = Math.min(curr[1], points[i++][1]);
            
            if(i < points.length){
                curr = points[i++];
                count++;
            }
        }
        
        return count;
    }
}
