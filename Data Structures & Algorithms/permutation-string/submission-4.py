from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1)
        count = {}
        l = 0
        for r, c in enumerate(s2):
            if c not in need:
                count = {}
                l = r + 1
                continue
            count[c] = count.get(c, 0) + 1
            while count[c] > need[c]:
                count[s2[l]] -= 1
                l += 1
            if r - l + 1 == len(s1):
                return True
        return False