class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (amount+1) for _ in range(len(coins)+1)]

        for i in range(len(coins)+1):
            dp[i][0] = 1


        for i in range(len(coins)-1, -1, -1):
            for a in range(1, amount+1):
                choice1 = 0
                if coins[i] <= a:
                    choice1 = dp[i][a-coins[i]]
                choice2 = dp[i+1][a]
                max_val = choice1 + choice2
                dp[i][a] = max_val
        return dp[0][amount]