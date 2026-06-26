"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

        Sort meetings by start time. Keep a min-heap containing the end times of meetings currently using rooms.

For each new meeting:

Remove every meeting that already ended. Those rooms are now free.
Add the new meeting’s end time.
The heap size is the number of rooms currently occupied.
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda meeting: meeting.start)

        active_end_times = []
        max_rooms = 0

        for meeting in intervals:
            # Free every room whose meeting has ended
            while active_end_times and active_end_times[0] <= meeting.start:
                heapq.heappop(active_end_times)

            # Give the current meeting a room
            heapq.heappush(active_end_times, meeting.end)

            max_rooms = max(max_rooms, len(active_end_times))

        return max_rooms