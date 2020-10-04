class Solution {
    private boolean dfs(TreeNode root, int v) {
        if(root == null) return true;
        if(root.val != v) return false;
        return dfs(root.left, v) && dfs(root.right, v);
    }
    
    
    public boolean isUnivalTree(TreeNode root) {
        if(root == null) return true;
        int rootVal = root.val;
        return dfs(root, rootVal);   
    }
}


