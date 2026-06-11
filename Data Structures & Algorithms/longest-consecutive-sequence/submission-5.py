class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        arr = set(nums)
        new_arr = list(arr)
        new_arr.sort()
        print(new_arr)
        length = len(new_arr)
        i = 0
        count = 1
        max_val = 0

        while i < length - 1:
            if new_arr[i+1] == new_arr[i] + 1:
                count += 1
            if new_arr[i+1] != new_arr[i] + 1:
                max_val = max(max_val, count)
                count = 1
            i += 1
        max_val = max(max_val, count)
        return max_val


