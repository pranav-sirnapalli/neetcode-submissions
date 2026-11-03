class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dp(i, remaining):
            if remaining == 0:
                return 1
            
            elif remaining < 0 or i >= len(coins):
                return 0

            elif (i, remaining) in memo:
                return memo[i, remaining]
            
            else:
                choice1 = dp(i, remaining-coins[i])
                choice2 = dp(i+1, remaining)
                total = choice1+choice2
                memo[i, remaining] = total
                return memo[i, remaining]

        return dp(0, amount)