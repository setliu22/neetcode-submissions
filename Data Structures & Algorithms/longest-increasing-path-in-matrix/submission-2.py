"""
longestFrom(r, c)

From (r, c), inspect all four neighbors.

If a neighbor is larger, we can move there:
1 + longestFrom(neighbor)

If there are multiple larger neighbors, take the maximum.

If there are no larger neighbors, the answer is 1, because the path contains only the current cell.

Once we calculate:

longestFrom(r, c)

we store it. If another path reaches (r, c), we reuse the saved answer instead of recalculating everything from that cell.

So best = 1 is the base value.

The cache starts empty. Values are filled only when longestFrom(r, c) is called.

Outer loop order: top-left to bottom-right
DP calculation order: follows increasing paths as needed
"""

from functools import cache
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
        ]

        @cache
        def longestFrom(r: int, c: int) -> int:
            best = 1

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and matrix[nr][nc] > matrix[r][c]
                ):
                    best = max(
                        best,
                        1 + longestFrom(nr, nc)
                    )

            return best

        answer = 0

        for r in range(rows):
            for c in range(cols):
                answer = max(answer, longestFrom(r, c))

        return answer  