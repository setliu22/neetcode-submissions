"""
Do not try all possible trees.
Grow one tree, one cheapest safe edge at a time.
A true brute force solution would try every possible way to connect the points, which is enormous.

adding one thing at a time like go through all unconnected, and for each unconnected, link to a connected

For every unconnected point:
    find its cheapest edge to any connected point

Pick the unconnected point with the cheapest such edge
Add it to connected

speedup strategy:
we don't need to check 0 again after we do it the first time, we only need to check with what we add
"""

from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        # in_mst[i] means point i is already connected to the tree
        in_mst = [False] * n

        # min_dist[i] = cheapest cost to connect point i to the current tree
        min_dist = [float("inf")] * n

        # Start from point 0 with cost 0
        min_dist[0] = 0

        total_cost = 0

        for _ in range(n):
            curr = -1
            curr_cost = float("inf")

            # Find the unconnected point with the cheapest connection cost
            for i in range(n):
                if not in_mst[i] and min_dist[i] < curr_cost:
                    curr_cost = min_dist[i]
                    curr = i

            # Add that point to the MST
            in_mst[curr] = True
            total_cost += curr_cost

            x1, y1 = points[curr]

            # Update connection costs for all remaining points
            for j in range(n):
                if not in_mst[j]:
                    x2, y2 = points[j]
                    dist = abs(x1 - x2) + abs(y1 - y2)

                    # If connecting j through curr is cheaper, update it
                    if dist < min_dist[j]:
                        min_dist[j] = dist

        return total_cost