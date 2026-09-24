class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m = len(mat1)
        n = len(mat2[0])
        k = len(mat2)
        res = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                for x in range(k):
                    res[i][j] += mat1[i][x] * mat2[x][j]
        return res