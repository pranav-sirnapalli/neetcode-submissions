class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf")] * (n+1)
        dp[0] = 0
        squares = []

        for i in range(1, n+1):
            if (i * i) <= n:
                squares.append(i*i)
        #print(squares)

        for i in range(1, n+1):
            for square in squares:
                if square <= i:
                    dp[i] = min(dp[i], 1 + dp[i-square])        
        return dp[n]