"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x: x.start)

        # use min heap to track room you can place stuff in
        if not intervals:
            return 0

        heap = [intervals[0].end] # initialize with first end

        n = len(intervals)

        ans = 1 # at least 1 room

        for i in range(1, n):
            interval = intervals[i]

            if interval.start < heap[0]: # new room needed smh
                ans += 1
                heapq.heappush(heap, interval.end)
            else: # you can use an existing room
                heapq.heappop(heap) # remove and push the room's new right side
                heapq.heappush(heap, interval.end)
            
        return ans