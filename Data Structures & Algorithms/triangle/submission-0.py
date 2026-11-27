class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        def dp(i, j):
            if i >= len(triangle):
                return 0

            elif (i, j) in memo:
                return memo[i, j]

            else:
                down = dp(i+1, j) 
                right = dp(i+1, j+1)
                total = triangle[i][j] + min(down, right)
                memo[i, j] = total
                return memo[i, j]

        return dp(0, 0)