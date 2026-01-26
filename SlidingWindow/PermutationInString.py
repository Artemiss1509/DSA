import collections
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        
        s1_count = collections.Counter(s1)
        window_count = collections.Counter()
        
        for i, char in enumerate(s2):
            window_count[char] += 1
            
            # Remove character that's outside the window
            if i >= len(s1):
                left_char = s2[i - len(s1)]
                window_count[left_char] -= 1
                if window_count[left_char] == 0:
                    del window_count[left_char]
            
            # Check if window matches s1
            if i >= len(s1) - 1 and s1_count == window_count:
                return True
        
        return False