# dist stores nodes whose shortest time is finalized

# dist: Nodes whose shortest time is finalized.
# heap: Possible next nodes to finalize, ordered by smallest time.

"""
You do not finalize a node when you first discover it.

You only finalize it when it comes out of the heap.

if it came out of the heap, it means it was eventually the min

you are slowly building what you know for sure works, you can add 3 because the start node is automatically part of the working graph and there is no faster way to get there

From node 3, we discover a better way to node 2 and we add to the heap

and if a node already in finalized just pop when you encounted later in the heap
"""

import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))

        heap = [(0, k)]
        dist = {}

        while heap:
            time, node = heapq.heappop(heap)

            if node in dist:
                continue

            dist[node] = time

            for nei, weight in graph[node]:
                if nei not in dist:
                    heapq.heappush(heap, (time + weight, nei))

        if len(dist) != n:
            return -1

        return max(dist.values())