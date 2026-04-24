class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        max_val = 0
        while i < j:
            height = min(heights[i], heights[j]) * (j-i)
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
            
            max_val = max(max_val, height)
        return max_val
