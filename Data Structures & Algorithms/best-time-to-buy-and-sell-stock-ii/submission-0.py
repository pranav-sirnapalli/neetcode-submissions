class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dp(day, holding):
            if day == len(prices):
                return 0

            if (day, holding) in memo:
                return memo[(day, holding)]
            

            if not holding:
                buy = -prices[day] + dp(day+1, True)
                skip = dp(day+1, False)
                profit = max(buy, skip)        
            
            else:
                sell = prices[day] + dp(day+1, False)
                skip = dp(day+1, True)
                profit = max(sell, skip)
            memo[(day, holding)] = profit
            return profit
        return dp(0, False)