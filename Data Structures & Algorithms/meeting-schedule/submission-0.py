"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

Solution

Sort meetings by start time. Then each meeting only needs to be compared with the meeting directly before it.

After sorting, if:

current start < previous end

they overlap.

Meeting Rooms:
"Does any overlap exist?"
No choice is involved.
Sort by start to examine the schedule chronologically.

Non-overlapping Intervals:
"Which intervals should I keep to maximize the number kept?"
A greedy choice is involved.
Sort by end so you always keep the interval that frees the timeline earliest.
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda meeting: meeting.start)

        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i - 1].end:
                return False

        return True