from collections import defaultdict, Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        target_counts = Counter(t)
        required = len(target_counts)
        
        left = 0
        formed = 0
        window_counts = defaultdict(int)
        
        min_window = (-1, 0, 0)
        
        for right, char in enumerate(s):
            window_counts[char] += 1
            
            if char in target_counts and window_counts[char] == target_counts[char]:
                formed += 1
            
            while left <= right and formed == required:
                if min_window[0] == -1 or (right - left + 1) < min_window[0]:
                    min_window = (right - left + 1, left, right)
                
                left_char = s[left]
                window_counts[left_char] -= 1
                
                if left_char in target_counts and window_counts[left_char] < target_counts[left_char]:
                    formed -= 1
                
                left += 1
        
        return "" if min_window[0] == -1 else s[min_window[1]:min_window[2] + 1]
        