class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dp(i, end):
            if i > end:
                return 0
            
            elif (i, end) in memo:
                return memo[(i, end)]
            
            else:
                rob1 = nums[i] + dp(i+2, end)
                next_house = dp(i+1, end)
                max_val = max(rob1, next_house)
                memo[(i, end)] = max_val
                return memo[(i, end)]

        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        return max(dp(0, len(nums)-2), dp(1, len(nums)-1))


