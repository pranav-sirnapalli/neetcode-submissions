class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            
            if total > target or i >= len(nums):
                return None
            
            curr.append(nums[i])
            backtrack(i, curr, nums[i] + total)
            curr.pop()
            backtrack(i+1, curr, total)

        backtrack(0, [], 0)
        return res
