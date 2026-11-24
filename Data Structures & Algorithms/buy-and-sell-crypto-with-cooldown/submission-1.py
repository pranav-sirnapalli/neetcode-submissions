class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * 2 for i in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, len(prices)):
            if i == 1:
                buy = -prices[i]
            else:
                buy = -prices[i] + dp[i-2][0]
            skip = dp[i-1][0]
            

            sell = prices[i] + dp[i-1][1]
            hold = dp[i-1][1]
            dp[i][1] = max(buy, hold)
            dp[i][0] = max(sell, skip)
        
        return dp[-1][0]