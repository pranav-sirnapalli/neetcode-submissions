class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = 1
        max_height = 0

        for i in range(len(heights)-1):
            for j in range(i+1, len(heights)):
                height = min(heights[i], heights[j]) * (j-i)
                max_height = max(max_height, height)
        
        return max_height

        