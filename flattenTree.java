class Solution {
    public void flatten(TreeNode root) {
        if(root == null){
            return;
        }
        
        flatten(root.left);
        flatten(root.right);
        
        TreeNode left = root.left;
        TreeNode right = root.right;
                
        root.right = left;
        root.left = null;
        TreeNode parent = root;
        if(right != null){
            while(parent.right != null){
                parent = parent.right;
            }
            parent.right = right;
        }
    }
}
