"""
Start by finding a stored point directly above or below the query:

query:          (x, y)
vertical point: (x, y2)

That determines the side length:

side = abs(y2 - y)

The other side of the square must be exactly side units left or right:

x2 = x + side

or:

x2 = x - side

Then check whether these two points exist:

(x2, y)
(x2, y2)
"""

from collections import defaultdict, Counter
from typing import List

class CountSquares:

    def __init__(self):
        self.points = defaultdict(Counter)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[x][y] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        total = 0

        # Try every stored point above or below the query
        for y2, count_vertical in self.points[x].items():
            if y2 == y:
                continue

            side = abs(y2 - y)

            # Square can extend left or right
            for x2 in (x - side, x + side):
                total += (
                    count_vertical
                    * self.points[x2][y]
                    * self.points[x2][y2]
                )

        return total
