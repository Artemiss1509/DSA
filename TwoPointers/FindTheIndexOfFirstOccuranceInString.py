class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        left=0
        right=0
        while left<len(haystack):

            if needle[right]==haystack[left]:
                right+=1
                left+=1
            elif needle[right]!=haystack[left]:
                left= left-right
                left+=1
                right=0
            if right>=len(needle):
                return (left-right)
        return -1
        