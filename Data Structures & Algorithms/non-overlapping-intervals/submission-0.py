"""
Touching is allowed

Solution

Always keep the interval that ends earliest.

Why? It leaves the most space for intervals that come later.

First sort by ENDING TIME:

[[1,2], [2,4], [1,4]]

Then:

Keep [1,2]

[2,4] starts at 2, and the previous interval ends at 2, so keep it.

Keep [2,4]

[1,4] starts at 1, but the previous kept interval ends at 4, so they overlap.

Remove [1,4]
"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[1])

        removals = 0
        previous_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start < previous_end:
                removals += 1
            else:
                previous_end = end

        return removals  