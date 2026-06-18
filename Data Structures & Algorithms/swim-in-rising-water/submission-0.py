from typing import List
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # heap item = (minimum time needed to reach this cell, row, col)
        heap = [(grid[0][0], 0, 0)]

        visited = set()

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while heap:
            time, row, col = heapq.heappop(heap)

            if (row, col) in visited:
                continue

            visited.add((row, col))

            # The first time we pop the bottom-right cell,
            # we found the minimum possible max elevation path.
            if row == n - 1 and col == n - 1:
                return time

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    new_time = max(time, grid[nr][nc])
                    heapq.heappush(heap, (new_time, nr, nc))