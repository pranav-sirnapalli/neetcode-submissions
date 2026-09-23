class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max_num = len(nums)
        net_sum = 0
        for i in range(1, max_num+1):
            net_sum = net_sum + i
        
        total_sum = sum(nums)
        value = (net_sum - total_sum)
        return int(value)