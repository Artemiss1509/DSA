class Solution:
    def longestPalindrome(self, s: str) -> str:

        def checkPal(s,left,right):
            while left>=0 and right <len(s) and s[left]==s[right]:
                left-=1
                right+=1
                
            return s[left+1:right]

        ans = ''
        for i in range(len(s)):
            ans = ans if len(ans)>len(checkPal(s,i,i)) else checkPal(s,i,i)
            ans = ans if len(ans)>len(checkPal(s,i,i+1)) else checkPal(s,i,i+1)
        return ans
