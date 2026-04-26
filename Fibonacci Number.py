class Solution:
    def fib(self, n: int) -> int:
        memo = {0: 0, 1: 1}
        
        def dfs(k):
            if k not in memo:
                memo[k] = dfs(k - 1) + dfs(k - 2)
            return memo[k]
        
        return dfs(n)
