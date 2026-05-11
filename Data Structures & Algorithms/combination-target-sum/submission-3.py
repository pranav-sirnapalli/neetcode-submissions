class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, curr, value):
            if value == target:
                res.append(curr.copy())
                return
            
            if i >= len(nums) or value > target:
                return None
            

            curr.append(nums[i])
            dfs(i, curr, nums[i] + value)
            curr.pop()
            dfs(i + 1, curr, value)
            
        dfs(0, [], 0)
        return res