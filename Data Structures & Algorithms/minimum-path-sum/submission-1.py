class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #dp = [[0] * len(grid) for i in range(len(grid[0]))]
        rows, cols = len(grid), len(grid[0])
        dp = [[0] * cols for i in range(rows)]
        dp[rows-1][cols-1] = grid[rows-1][cols-1]
        
        
        for r in range(rows-1, -1, -1):
            for c in range(cols-1, -1, -1):
                if r == rows-1 and c == cols-1:
                    continue
                right_val = float("inf")
                bottom_val = float("inf")
                if c+1 < cols:
                    right_val = dp[r][c+1]
                if r+1 < rows:
                    bottom_val = dp[r+1][c]
                dp[r][c] = grid[r][c] + min(right_val, bottom_val)
        return dp[0][0]