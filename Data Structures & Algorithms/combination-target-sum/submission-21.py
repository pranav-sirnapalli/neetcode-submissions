class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def combination(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            
            if total > target or i >= len(nums):
                return None

            curr.append(nums[i])
            combination(i, curr, total+nums[i])
            curr.pop()
            combination(i+1, curr, total)

        combination(0, [], 0)
        return res
