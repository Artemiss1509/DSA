class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {}
        for i in range(len(order)):
            d[order[i]]= i

        for i in range(len(words)-1):
            for j in range(len(words[i])):
                if j >= len(words[i+1]):
                    return False
                if words[i][j] != words[i+1][j]:
                    current = d[words[i][j]]
                    nextWord = d[words[i+1][j]]
                    if(nextWord<current):
                        return False
                    else:
                        break
        return True