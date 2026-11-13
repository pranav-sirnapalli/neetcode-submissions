class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])
        houses1 = nums[:-1]
        dp1 = [0] * len(houses1)
        dp1[0] = houses1[0]
        dp1[1] = max(houses1[0], houses1[1])

        houses2 = nums[1:]
        dp2 = [0] * len(houses2)
        dp2[0] = houses2[0]
        dp2[1] = max(houses2[0], houses2[1])

        for i in range(2, len(houses1)):
            rob = houses1[i] + dp1[i-2]
            skip = dp1[i-1]
            dp1[i] = max(rob, skip)
        

        for i in range(2, len(houses2)):
            rob = houses2[i] + dp2[i-2]
            skip = dp2[i-1]
            dp2[i] = max(rob, skip)
        return max(dp1[-1], dp2[-1])