"""
        lst = []
        for i in intervals:
            lst.append((i.start, i.end))

        q = deque(lst.sort())

        while q:
            res += 1
            c, d = q.popleft()
            while b > c:
                c, d = q.popleft()
                b = max(b, d)
            a = c
        
        return res
"""

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        if len(intervals) == 0:
            return 0
            
        intervals.sort(key = lambda meeting: meeting.start)
    
        heap = [intervals[0].end]

        for i in range(1, len(intervals)):
            interval = intervals[i]

            #end_time = heapq.heappop(heap)
            if interval.start < heap[0]:
                heapq.heappush(heap, interval.end)
            else:
                heapq.heappop(heap)
                heapq.heappush(heap, interval.end)
        
        return len(heap)
