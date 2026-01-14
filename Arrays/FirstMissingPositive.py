from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Step 1: Check if 1 exists
        if 1 not in nums:
            return 1
        
        # Step 2: Clean up the array
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
        
        # Step 3: Use indices to mark presence
        for i in range(n):
            idx = abs(nums[i])
            if idx == n:
                nums[0] = -abs(nums[0])
            else:
                nums[idx] = -abs(nums[idx])
        
        # Step 4: Find the first missing positive
        for i in range(1, n):
            if nums[i] > 0:
                return i
        
        if nums[0] > 0:
            return n
        
        return n + 1