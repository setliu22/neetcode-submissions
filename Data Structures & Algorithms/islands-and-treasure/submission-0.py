from collections import deque
from typing import List


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        columns = len(grid[0])
        queue = deque()

        # Add every treasure chest as a BFS starting point.
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == 0:
                    queue.append((row, column))

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
        ]

        while queue:
            row, column = queue.popleft()

            for row_change, column_change in directions:
                next_row = row + row_change
                next_column = column + column_change

                if (
                    next_row < 0
                    or next_row >= rows
                    or next_column < 0
                    or next_column >= columns
                    or grid[next_row][next_column] != 2147483647
                ):
                    continue

                grid[next_row][next_column] = grid[row][column] + 1
                queue.append((next_row, next_column))