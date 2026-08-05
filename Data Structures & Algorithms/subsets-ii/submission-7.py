class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def subsets(curr, i):
            if i == len(nums):
                res.append(curr.copy())
                return
            
            curr.append(nums[i])
            subsets(curr, i+1)
            curr.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            subsets(curr, i+1)

        subsets([], 0)
        return res