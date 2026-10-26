class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dp(i):
            if i >= len(nums):
                return 0
            
            elif i in memo:
                return memo[i]


            else:
                rob1 = nums[i] + dp(i+2)
                next_house = dp(i+1)
                max_val = max(rob1, next_house)
                memo[i] = max_val
                return memo[i]


        return dp(0)