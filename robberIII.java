class Solution {
    public int rob(TreeNode root) {
        // each thing returns two values
        int[] result = robbing(root);
        
        return (result[0] > result[1]) ? result[0] : result[1];
    }
  
    private int[] robbing(TreeNode curr){
        
        int[] res = {0, 0};
        
        if(curr == null) {
            return res;
        }
        
        int[] left = robbing(curr.left);
        int[] right = robbing(curr.right);
        
        int bestLeft = (left[0] > left[1]) ? left[0] : left[1];
        int bestRight = (right[0] > right[1]) ? right[0] : right[1];
        
        res[0] = left[1]+right[1]+curr.val;
        res[1] = bestLeft+bestRight;
        
        return res;
    }
}

