class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        memo = {}
        points = {}

        for i in nums:
            if i in points:
                points[i] += i
            else:
                points[i] = i
        
        def dp(i):
            if i > max(nums):
                return 0
            
            elif i in memo:
                return memo[i]
            
            else:
                choice1 = points.get(i, 0) + dp(i+2)
                choice2 = dp(i+1)
                max_val = max(choice1, choice2)
                memo[i] = max_val
                return memo[i]      

        return dp(min(nums))