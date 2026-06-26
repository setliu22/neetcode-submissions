"""
Efficient idea

Process queries from smallest to largest.

For each query q:

Add every interval whose start is <= q.
Remove intervals whose end is < q, because they can no longer contain q.
Among the remaining intervals, choose the shortest one.

Use a min-heap storing:

(interval length, interval end)

The shortest candidate is always at the top.
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