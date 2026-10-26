class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}


        def dp(i):
            if i >= len(nums):
                return 0
            
            elif i in memo:
                return memo[i]
            
            else:
                buy = nums[i] + dp(i+2)
                sell = dp(i+1)
                max_val = max(buy, sell)
                memo[i] = max_val
                return memo[i]

        return dp(0)
        