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
        
        minsum = [[grid[0][0]] * n for row in range(m)]
        
        for i in range(1, m):
            minsum[i][0] = minsum[i-1][0] + grid[i][0]
        for j in range(1, n):
            minsum[0][j] = minsum[0][j-1] + grid[0][j]
        
        for i in range(1, m):
            for j in range(1, n):
                minsum[i][j] = min(minsum[i-1][j], minsum[i][j-1]) + grid[i][j]
        
        return minsum[m-1][n-1]
