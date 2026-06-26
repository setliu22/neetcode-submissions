"""
We use <= because touching intervals overlap here. For example, [1,2] and [2,3] overlap.
also, intervals are already sorted
"""

class Solution:
    def insert(
        self,
        intervals: List[List[int]],
        newInterval: List[int]
    ) -> List[List[int]]:

        result = []
        i = 0
        n = len(intervals)

        # 1. Add intervals completely before newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # 2. Merge every overlapping interval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        result.append(newInterval)

        # 3. Add intervals completely after newInterval
        while i < n:
            result.append(intervals[i])
            i += 1

        return result