class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()

        while len(stones) > 1:
            v1, v2 = stones[-1], stones[-2]
            val = v1 - v2
            del stones[-1]
            del stones[-1]
            if val > 0:
                stones.append(val)
            stones.sort()
        return sum(stones)
