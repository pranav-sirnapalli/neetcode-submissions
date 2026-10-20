class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        #pass
        total_sum = sum(nums)
        prefix = 0
        suffix = 0
        answer = float("-inf")

        for i in nums:
            prefix += i
            suffix = total_sum - prefix + i
            answer = max(answer, prefix, suffix)
        return answer