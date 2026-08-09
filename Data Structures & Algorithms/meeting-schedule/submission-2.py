"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x: x.start)

        n = len(intervals)

        if not intervals:
            return True

        maxfromleft = intervals[0].end

        for i in range(1, n):
            interval = intervals[i]

            if interval.start < maxfromleft:
                return False
            else:
                maxfromleft = interval.end
            
        return True