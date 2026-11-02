class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dp(remaining):
            if remaining == 0:
                return 0
            
            elif remaining in memo:
                return memo[remaining]

            else:
                min_coins = float("inf")

                for coin in coins:
                    if coin <= remaining:
                        candidate = 1 + dp(remaining - coin)
                        min_coins = min(min_coins, candidate)
                memo[remaining] = min_coins
                return memo[remaining] 

        answer = dp(amount)
        if answer == float("inf"):
            return -1
        return answer