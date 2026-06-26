"""

You are given one list that may:

Be unsorted
Already contain many overlapping intervals

Example:

[[8,10], [1,3], [2,6], [15,18]]

First sort it:

[[1,3], [2,6], [8,10], [15,18]]

Then merge every overlapping pair:

[[1,6], [8,10], [15,18]]

"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        result = []

        for start, end in intervals:
            if not result or start > result[-1][1]:
                result.append([start, end])
            else:
                result[-1][1] = max(result[-1][1], end)

        return result