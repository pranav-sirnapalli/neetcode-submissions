class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        count = 0
        for i in nums:
            if i == target:
                count += 1
        
        if (len(nums) / 2) < count:
            return True
        return False