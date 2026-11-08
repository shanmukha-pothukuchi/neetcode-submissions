class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def get_time(m):
            res = 0
            for p in piles:
                res += math.ceil(p / m)
            return res

        l = 1
        r = max(piles)

        while l <= r:
            m = (l + r) // 2

            if get_time(m) > h:
                l = m + 1
            else:
                r = m - 1

        return l