class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * cols for i in range(rows)]
        if obstacleGrid[rows-1][cols-1] == 1:
            dp[rows-1][cols-1] = 0
        else:
            dp[rows-1][cols-1] = 1
        for r in range(rows-1, -1, -1):
            for c in range(cols-1, -1, -1):
                right = 0
                bottom = 0
                if r == rows-1 and c == cols-1:
                    continue
                if obstacleGrid[r][c] == 1:
                    continue
                if c + 1 < cols:
                    right = dp[r][c+1]
                if r + 1 < rows:
                    bottom = dp[r+1][c]
                dp[r][c] = right + bottom
        return dp[0][0]