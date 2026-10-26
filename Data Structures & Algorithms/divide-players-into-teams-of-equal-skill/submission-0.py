class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        total_sum = sum(skill)

        target = total_sum // (len(skill) // 2)

        cnt = Counter(skill)
        
        res = 0
        for v in skill:
            if cnt[v] == 0:
                continue
            w = target - v
            if cnt[w] == 0:
                return -1
            cnt[v] -= 1
            cnt[w] -= 1
            res += v * (target - v)

        return res