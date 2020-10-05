class Solution {
    public boolean isCompleteTree(TreeNode root) {
   
        boolean end = false; 
        
        Queue<TreeNode> q = new LinkedList(); 
        
        q.offer(root); 
        
        while(!q.isEmpty()){
            
            TreeNode n = q.poll(); 
            
             if(n == null) end = true ; 
             else {
                 if(end) return false;
                 
                 q.offer(n.left); 
                 q.offer(n.right); 
             }
        }
        
        return true; 
        
    }
}


