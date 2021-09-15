class Solution(object):
    def countNegatives(self, grid):
        
        r = len(grid)
        c = len(grid[0])
        
        n = 0
        
        for i in range(r):
            for j in range(c):
                if grid[i][j] < 0:
                    n+=1
        
        
        return n
       
        
        
