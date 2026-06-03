class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_Area = 0
        while left < right :
            current_Area = (right-left) * min(height[left],height[right])
            max_Area = max(max_Area, current_Area)
            if height[left] < height[right]:                
                left += 1
            else:
                right -= 1

        return max_Area
            


                 

