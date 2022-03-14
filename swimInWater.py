class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        uf = [[(i, j) for j in range(n)] for i in range(m)]
        def find(i, j):
            if not (i,j) == uf[i][j]:
                uf[i][j] = find(*uf[i][j])
            return uf[i][j]
        order = sorted((grid[i][j], i, j) for j in range(n) for i in range(m))
        for val, i, j in order:
            for ni, nj in [[i+1, j], [i-1,j], [i, j+1], [i, j-1]]:
                if (0<=ni<m) and (0<=nj<n) and grid[ni][nj] <= val:
                    ai, aj = find(i, j)
                    bi, bj = find(ni, nj)
                    uf[ai][aj] = uf[bi][bj]
            if find(0,0) == find(m-1, n-1):
                return val
