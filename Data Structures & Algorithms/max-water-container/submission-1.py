class Solution:
    def maxArea(self, heights: List[int]) -> int:

        #We will use two pointer for this question 
        
        L = 0
        R = len(heights) - 1
        maxWater = 0

        while L < R:
            width = R - L
            containerHeight = min(heights[L], heights[R])
            area = width * containerHeight

            maxWater = max(area, maxWater)

            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1

        return maxWater
        