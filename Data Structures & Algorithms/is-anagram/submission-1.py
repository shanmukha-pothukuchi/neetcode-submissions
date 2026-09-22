class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}

        for c in s:
            d[c] = d.get(c, 0) + 1

        for c in t:
            if c not in d:
                return False

            d[c] -= 1

            if d[c] == 0:
                del d[c]
        
        for i in d.keys():
            return False
        
        return True