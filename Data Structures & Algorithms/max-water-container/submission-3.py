class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxHolder = 0

        

            
        left = 0
        right = len(heights)-1

        while left <right:
            area = (right -left) * min(heights[right],heights[left])
            if area> maxHolder:
                maxHolder= area
            
            #move left pointer if it shorter
            if heights[left]< heights[right]:
                left+=1
            else:
                right-=1

        return maxHolder
