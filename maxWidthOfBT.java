class Solution {
    
    int maxWidth; 
    
    HashMap<Integer, Integer> leftmostPos; 
    
    public int widthOfBinaryTree(TreeNode root) {
        
         maxWidth = 0; 
        
        leftmostPos = new HashMap(); 
        
        getWidth(root, 0, 0); 
        
        return maxWidth; 
        
    }
    
    public void getWidth(TreeNode root, int depth , int pos){
        
        if(root==null) return; 
        
        leftmostPos.computeIfAbsent(depth, x -> pos ); 
        
        maxWidth = Math.max( maxWidth, pos - leftmostPos.get(depth) +1); 
        
        getWidth(root.left, depth +1, pos * 2); 
        
        getWidth(root.right, depth+1, pos * 2 + 1); 
        
        
    }
}
