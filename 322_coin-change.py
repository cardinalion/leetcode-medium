# Approach 1: dynamic programming

# Tips: no recursive calls, use for loop from 1 to target

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        arr = [amount+1] * (amount+1);
        arr[0] = 0;
        
        for i in range(1, amount+1):
            for coin in coins:
                if coin > i:
                    continue
                arr[i] = min(arr[i], arr[i-coin]+1)
                
        if arr[-1] == amount+1:
            return -1
        return arr[-1]
        
# Approach 2: BFS

# Approach 3: DFS
