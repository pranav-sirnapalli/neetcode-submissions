class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo = {}

        rows, cols = len(obstacleGrid), len(obstacleGrid[0])

        def dp(i, j):
            if i >= rows or j >= cols:
                return 0
            
            elif obstacleGrid[i][j] == 1:
                return 0

            elif i == rows-1 and j == cols-1:
                return 1
            
            elif (i, j) in memo:
                return memo[i, j]

            else:
                right = dp(i, j+1)
                down = dp(i+1, j)
                paths = right + down
                memo[i, j] = paths
                return memo[i, j]

        return dp(0, 0)