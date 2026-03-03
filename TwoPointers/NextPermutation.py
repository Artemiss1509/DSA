class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(nums,a,b):
            c = nums[a]
            nums[a] = nums[b]
            nums[b] = c
        
        def reverse(nums,a):
            nums[a:] = nums[a:][::-1]
        
        i = len(nums)-2
        while i>=0 and nums[i+1]<= nums[i]:
            i-=1
        if i>=0:
            j = len(nums)-1
            while nums[j]<= nums[i]:
                j-=1
            swap(nums, i,j)
        reverse(nums,i+1)