class Solution {
    public int rangeSumBST(TreeNode root, int L, int R) {
        int sum = 0; 
        Stack<TreeNode> s = new Stack(); 
        s.push(root);
        while(!s.isEmpty()){
            TreeNode n = s.pop(); 
            if(n != null){
                if(n.val >= L && n.val <= R) {
                    sum+= n.val; 
                }
                
                 if(n.val > L) s.push(n.left); 
                 if(n.val < R ) s.push(n.right); 
            }
        }
        return sum; 
    }
}
