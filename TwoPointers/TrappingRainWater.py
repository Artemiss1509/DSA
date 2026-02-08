class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n-1
        leftmax, rightmax = 0, 0
        currentWater = 0

        while left<=right:

            if height[left]<height[right]:
                if height[left]>leftmax:
                    leftmax = height[left]
                else:
                    currentWater += leftmax - height[left]
                left+=1
            else:
                if height[right]>rightmax:
                    rightmax = height[right]
                else:
                    currentWater += rightmax-height[right]
                right-=1
        return currentWater