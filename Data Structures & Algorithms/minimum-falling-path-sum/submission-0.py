class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        memo = {}
        rows, cols = len(matrix), len(matrix[0])
        def dp(r, c):
            if c < 0 or c >= cols:
                return float("inf")
                
            if r >= rows:
                return 0

            elif (r, c) in memo:
                return memo[(r, c)]
            
            else:
                path1 = dp(r+1, c-1)
                path2 = dp(r+1, c)
                path3 = dp(r+1, c+1)
                max_val = matrix[r][c] + min(path1, path2, path3)
                memo[r, c] = max_val
                return memo[r, c]

        res = float("inf")
        for c in range(0, cols):
            res = min(res, dp(0, c))
        return res
        #pass
