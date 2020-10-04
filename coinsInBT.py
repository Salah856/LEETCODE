class Solution:
    
    def distributeCoins(self, root):
        
        self.count = 0
        def postorder(root, parent):
            if not root: return
            
            postorder(root.left, root)
            postorder(root.right, root)
            
            if parent:
                parent.val = parent.val - (1 - root.val)
                self.count += abs(1-root.val)
            
        postorder(root, None)
        return self.count 
    
