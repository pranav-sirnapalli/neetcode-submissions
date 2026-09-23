class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        max_val = len(nums)

        for i in range(1, max_val+1):
            if i not in nums:
                res.append(i)
        return res
        