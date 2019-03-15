class Solution:
    def clumsy(self, N: int) -> int:
        
        def pair(N:int) -> int:
            return int(N*(N-1)/(N-2))
        
        left = N%4
        sum = 0
        
        if N < 3:
            return N
        if N == 3:
            return 6
        
        sum += pair(N) + N-3
        
        for i in range(N-4, 3, -4):
            sum -= pair(i) - i+3          
        
        if left == 1:
            return sum-1
        if left == 2:
            return sum-2
        if left == 3:
            return sum-6
        return sum
