# heapq is always min heap
# just make an initial heap, then for simulation just use the heap pop and heap insertion operations

import heapq
from typing import List

"""
You use heapify because you want to convert the entire list into a valid heap all at once. That takes O(n) time. Python’s heapq.heapify transforms a list into a heap in linear time.

In Kth Largest in a Stream, the construction is more specific because you only want to keep the largest k values, not every value. So you can build it by calling add() on each number:
"""

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            y = -heapq.heappop(heap)  # largest
            x = -heapq.heappop(heap)  # second largest

            if y != x:
                heapq.heappush(heap, -(y - x))

        return -heap[0] if heap else 0