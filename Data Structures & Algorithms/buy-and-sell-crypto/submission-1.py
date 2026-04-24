class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        max_val = 0
        while i < j and j < len(prices):
            if(prices[j] < prices[i]):
                i = j
                j += 1
            else:
                max_val = max(max_val, prices[j]-prices[i])
                j += 1
        return max_val