class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(subsets, i):
            if i == len(nums):
                res.append(subsets.copy())
                return
            
            subsets.append(nums[i])
            backtrack(subsets, i + 1)
            subsets.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(subsets, i + 1)

        backtrack([], 0)
        return res
