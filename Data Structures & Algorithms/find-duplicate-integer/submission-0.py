class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        found = set()
        
        for i in nums:
            if i not in found:
                found.add(i)
            else:
                return i
        return -1
        