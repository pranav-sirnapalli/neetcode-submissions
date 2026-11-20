class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dp(i, holding):
            if i == len(prices):
                return 0
            
            elif (i, holding) in memo:
                return memo[(i, holding)]
            
            else:
                if holding:
                    sell = prices[i] + dp(i+1, False)
                    skip = dp(i+1, True)
                    max_val = max(sell, skip)
                    memo[(i, holding)] = max_val
                    return memo[(i, holding)]
                
                else:
                    buy = -prices[i] + dp(i+1, True)
                    skip = dp(i+1, False)
                    max_val = max(buy, skip)
                    memo[(i, holding)] = max_val
                    return memo[(i, holding)]

        return dp(0, False)