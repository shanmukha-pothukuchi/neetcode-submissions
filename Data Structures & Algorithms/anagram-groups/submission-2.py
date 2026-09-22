class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for s in strs:
            letters = [0] * 26
            for i, c in enumerate(s):
                letters[ord(c) - ord('a')] += 1
            k = tuple(letters)
            if k not in d:
                d[k] = []
            
            d[k].append(s)
        
        return list(d.values())