class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        sum_array = sum(nums)
        res = 0

        for i in range(0, max(nums)+1):
            res = res + i
        
        if sum_array == res:
            if 0 in nums:
                return len(nums)
            else:
                return 0

        else:
            return res - sum_array
        