class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = {}
        for i in nums:
            if i in res.keys():
                res[i] += 1
            else:
                res[i] = 1
        
        max_val = 0
        max_key = 0
        for i in res.keys():
            if res[i] > max_val:
                max_val = res[i]
                max_key = i
        return max_key