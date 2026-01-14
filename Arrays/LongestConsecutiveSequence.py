class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        count = 0
        for i in hashSet:
            if i-1 not in hashSet:
                lms = 1
                while i+1 in hashSet:
                    lms+=1
                    i+=1
                count = lms if lms>count else count
        return count