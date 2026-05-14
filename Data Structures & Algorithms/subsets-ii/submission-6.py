class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(subsets, i):
            if i == len(nums):
                res.append(subsets.copy())
                return
            
            subsets.append(nums[i])
            dfs(subsets, i + 1)
            subsets.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(subsets, i + 1)

        dfs([], 0)
        return res
