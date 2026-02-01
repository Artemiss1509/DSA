class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)==1:
            return True
        left=0
        right=len(s)-1
        while left<=right:
            
            while left<len(s) and not s[left].isalnum():
                left+=1
            while right>-1 and not s[right].isalnum():
                right-=1
            if left>len(s)-1 or right<0:
                continue
            if s[left].lower() == s[right].lower():
                left+=1
                right-=1
            else:
                return False
        return True