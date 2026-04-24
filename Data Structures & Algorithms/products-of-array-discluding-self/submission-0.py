class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_array = []
        r_array = []
        val = 1

        for i in nums:
            val = val * i
            l_array.append(val)
        
        length = len(nums)-1

        val = 1
        while length >= 0:
            val = val * nums[length]
            r_array.append(val)
            length -= 1
        r_array = r_array[::-1]

        res = [0] * len(nums)
        res[0] = r_array[1]
        
        for i in range(1, len(res)-1):
            res[i] = l_array[i-1] * r_array[i+1]
        res[len(res)-1] = l_array[len(l_array)-2]

        return res