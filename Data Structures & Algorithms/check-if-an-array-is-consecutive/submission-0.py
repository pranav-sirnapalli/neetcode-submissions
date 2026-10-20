class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        if len(nums) == 0 or len(nums) == 1:
            return True
        
        nums.sort()
        start = nums[0]


        for i in range(1, len(nums)):
            if nums[i] == start + 1:
                start = nums[i]
            else:
                return False
        return True

