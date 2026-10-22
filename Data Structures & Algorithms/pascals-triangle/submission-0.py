class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        
        if numRows == 1:
            return [[1]]

        res = [[1], [1, 1]]

        i = 2

        while i < numRows:
            dp = [1, 1]
            j = 0
            while j < len(res[-1]) - 1:
                dp.insert(-1, res[-1][j] + res[-1][j+1])
                j += 1

            res.append(dp)
            i += 1
        return res
