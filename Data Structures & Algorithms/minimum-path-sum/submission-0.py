class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = {}
        rows, cols = len(grid), len(grid[0])

        def dp(i, j):
            if i >= rows or j >= cols:
                return float("inf")
            
            elif i == rows-1 and j == cols-1:
                return grid[i][j]

            elif (i, j) in memo:
                return memo[i, j]
            
            else:
                right_path = dp(i, j+1)
                bottom_path = dp(i+1, j)
                cost = grid[i][j] + min(right_path, bottom_path)
                memo[i, j] = cost
                return memo[i, j]

        return dp(0, 0)