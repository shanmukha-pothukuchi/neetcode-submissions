class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0

        found = set()
        res = 0
        for r in range(len(s)):
            while s[r] in found:
                found.remove(s[l])
                l += 1
            found.add(s[r])
            res = max(r - l + 1, res)
        
        return res