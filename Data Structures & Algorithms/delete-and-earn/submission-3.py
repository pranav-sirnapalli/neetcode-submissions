class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        points = {}

        for i in nums:
            if i in points:
                points[i] += i
            else:
                points[i] = i
        dp = [0] * (max(nums)+1)
        dp[0] = 0
        dp[1] = points.get(1, 0)

        for i in range(2, len(dp)):
            choice1 = points.get(i, 0) + dp[i-2]
            choice2 = dp[i-1]
            max_val = max(choice1, choice2)
            dp[i] = max_val
        return dp[-1]