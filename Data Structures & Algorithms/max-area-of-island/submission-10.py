class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0

            curr_area = 1
            curr_area += dfs(r + 1, c)
            curr_area += dfs(r - 1, c)
            curr_area += dfs(r, c + 1)
            curr_area += dfs(r, c - 1)
            return curr_area


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    curr_area = dfs(r, c)
                    max_area = max(curr_area, max_area)
                    
        return max_area
