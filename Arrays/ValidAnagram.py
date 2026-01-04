class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        d=dict.fromkeys(['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m'], 0)
        
        for i,j in zip(s,t):
            d[i] += 1
            d[j] -= 1
           
        all_zeros = all(value == 0 for value in d.values())
        return all_zeros