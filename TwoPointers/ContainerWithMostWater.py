class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        max_height = 0
        while left<right:
            new_height=0
            if height[left]<height[right]:
                new_height = height[left] * (right-left)
                left+=1
            else:
                new_height = height[right] * (right-left)
                right-=1
            
            max_height = new_height if new_height>max_height else max_height
        return max_height