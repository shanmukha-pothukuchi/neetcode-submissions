import bisect

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        starts = [x for x, _ in intervals]
        ends = [y for _, y in intervals]

        start, end = newInterval

        left = bisect.bisect_left(ends, start)
        right = bisect.bisect_right(starts, end)

        if left < right:
            start = min(start, intervals[left][0])
            end = max(end, intervals[right - 1][1])

        return intervals[:left] + [[start, end]] + intervals[right:]