class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        tot = {}

        for i in nums:
            if i in tot.keys():
                tot[i] += 1
            else:
                tot[i] = 1

        for key in tot:
            if tot[key] == 1:
                return key