class Solution:
    
    def height(self, root):
        if root is None:
            return 1
        
        return max(self.height(root.left), self.height(root.right)) + 1
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if root is None:
            return True
        
        lh = self.height(root.left)
        rh = self.height(root.right)
        
        if abs(lh - rh) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        
        return False 


