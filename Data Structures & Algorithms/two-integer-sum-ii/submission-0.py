class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(numbers)-1):
            for j in range(i+1, len(numbers)):
                if target == numbers[i] + numbers[j]:
                    return [i+1, j+1]
        return []