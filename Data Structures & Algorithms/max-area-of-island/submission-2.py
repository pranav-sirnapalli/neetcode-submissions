class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return None

        rows, cols = len(grid), len(grid[0])
        max_area = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0

            current_area = 1
            current_area += dfs(r + 1, c)
            current_area += dfs(r - 1, c)
            current_area += dfs(r, c + 1)
            current_area += dfs(r, c - 1)
            return current_area


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    current_area = dfs(r, c)
                    max_area = max(current_area, max_area)
        return max_area