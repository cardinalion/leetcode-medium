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
# minimum path, iterate over levels

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:   
        
        covered, covering = [0]
        count =  0
        visited = [False] * (amount+1)
        visited[0] = True
        
        while covered:
            count += 1
            for v in covered:
                for coin in coins:
                    newval = v + coin
                    if newval <= amount:
                        if not visited[newval]:
                            if newval == amount:
                                return count
                            visited[newval] = True
                            covering.append(newval)
            covered, covering = covering, []
        return -1
    

# Approach 3: DFS
# Use the large-denomitation coins first, stop till unreplacable (must use more)
# Tips: distinguish the boundaries and iterators

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:   
        coins.sort(reverse=True)
        self.res = 2**31-1
        l = len(coins)
        
        def dfs(num, remain, count):
            if not remain:
                self.res = min(count, self.res)
            
            for j in range(num, l):
                if coins[j] <= remain < coins[j] * (self.res-count):
                    dfs(j, remain-coins[j], count+1)
        
        for i in range(l):
            dfs(i, amount, 0)
        
        return self.res if self.res != 2**31-1 else -1
    
