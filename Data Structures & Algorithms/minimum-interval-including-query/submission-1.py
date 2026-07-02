"""
Sort queries even though you need to paste in the correct order
Intervals not guaranteed to be sorted so sort those too

Add if left is <= q (which benefits future queries)
Remove if right is < q (which benefits future queries)

Only remove if right violates, otherwise min answer can apply to multiple
"""

import heapq

class Solution:
    def minInterval(
        self,
        intervals: List[List[int]],
        queries: List[int]
    ) -> List[int]:

        intervals.sort()
        sorted_queries = sorted(queries)

        heap = []
        answers = {}
        i = 0

        for q in sorted_queries:
            # Add intervals that have started
            while i < len(intervals) and intervals[i][0] <= q:
                left, right = intervals[i]
                length = right - left + 1
                heapq.heappush(heap, (length, right))
                i += 1

            # Remove intervals that ended before q
            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            # Shortest valid interval
            answers[q] = heap[0][0] if heap else -1

        return [answers[q] for q in queries]