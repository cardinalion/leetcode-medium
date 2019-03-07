class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        midint = int(n/2)
        for i in range(midint):
            for j in range (i, n-i-1):
                print(matrix[i][j],matrix[j][n-1-i],matrix[n-1-i][n-1-j],matrix[n-1-j][i])
                matrix[i][j],matrix[j][n-1-i],matrix[n-1-i][n-1-j],matrix[n-1-j][i] = matrix[n-1-j][i],matrix[i][j],matrix[j][n-1-i],matrix[n-1-i][n-1-j]
