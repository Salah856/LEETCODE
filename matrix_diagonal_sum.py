class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        s = 0
        
        for x in range(len(mat)):
            s += mat[x][x] + mat[x][-x-1]
        
        if len(mat) % 2 != 0:
            s -= mat[len(mat)//2][len(mat)//2]
        
        return s
