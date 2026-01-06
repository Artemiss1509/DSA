class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}

        for s in strs:
            # Sort the string to use as key
            key = ''.join(sorted(s))
            if key not in anagram_map:
                anagram_map[key] = []  # create a new list if key does not exist
            anagram_map[key].append(s)

        # Return all grouped anagrams
        return list(anagram_map.values())