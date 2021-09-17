class Solution:
    
    def __init__(self):
        self.visited = dict()
    
    
    def cloneGraph(self, node):
        if node:
            return self.cloneNode(node)
    
    
    def cloneNode(self, node):
		# Node visited case
        
        if node.val in self.visited:
            return self.visited[node.val]
        
        else:
            newNode = Node(node.val)
            self.visited[node.val] = newNode
            for nbr in node.neighbors:
                newNode.neighbors.append(self.cloneNode(nbr))
            
            return newNode
