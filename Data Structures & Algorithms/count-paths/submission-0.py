class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def dp(i, j):
            if i >= m or j >= n:
                return 0
            
            elif i == m-1 and j == n-1:
                return 1
            
            elif (i, j) in memo:
                return memo[i, j]
            
            else:
                right = dp(i, j+1)
                down = dp(i+1, j)
                total_paths = right + down
                memo[i, j] = total_paths
                return memo[i, j]

        return dp(0, 0)