import heapq

"""
We sort intervals by start time and queries in ascending order. For each query, we move index right to add every interval that has started into a min heap ordered by length, even if it's a long interval like [2,300] that might be useful later. Then we remove intervals from the top of the heap if they've expired (their end is smaller than the current query), because queries only increase, so expired intervals can never be useful again. We don't need to remove expired intervals buried in the heap until they reach the top. After that, the top of the heap contains the smallest interval covering the current query, or the heap is empty and the answer is -1. Finally, we restore the original query order.
"""

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # sort intervals and sort queries
        # ALWAYS sort intervals
        # move index right if start is at most the new query and size is smaller
        # otherwise keep the current index (cuz it could be like [2, 300])

        intervals.sort()
        queriescopy = queries[:]
        queries.sort()

        index = 0
        q_index = 0

        heap = []

        ans = {}

        n = len(queries)
        m = len(intervals)

        def int_len(interval):
            return interval[1] - interval[0] + 1
        
        while q_index < n:
            query = queries[q_index]

            while index < m and query >= intervals[index][0]:
                heapq.heappush(heap, (int_len(intervals[index]), intervals[index]))
                index += 1
            
            while heap and heap[0][1][1] < query: # if right side too small it won't work for the rest
                heapq.heappop(heap)

            if heap:
                ans[query] = heap[0][0]
            if not heap:
                ans[query] = -1
            
            q_index += 1
        
        print(ans)
        
        ans2 = []

        for query in queriescopy:
            ans2.append(ans[query])

        return ans2
