class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        if m == 0:
            return 0
        if m == 1:
            sumn = 0
            for k in range(n):
                sumn += grid[0][k]
            return sumn
        if n == 1:
            summ = 0
            for k in range(m):
                summ += grid[k][0]
            return summ
        
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        for j in range(1, n):
            grid[0][j] += grid[0][j-1]
        
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        
        return grid[m-1][n-1]
