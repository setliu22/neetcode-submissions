from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])

        queue = deque()
        fresh_fruit = 0

        # Add every initially rotten fruit to the queue.
        # Also count how many fresh fruits must eventually rot.
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == 2:
                    queue.append((row, column))
                elif grid[row][column] == 1:
                    fresh_fruit += 1

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
        ]

        minutes = 0

        # Process one BFS layer per minute.
        while queue and fresh_fruit > 0:
            fruits_in_current_minute = len(queue)

            for _ in range(fruits_in_current_minute):
                row, column = queue.popleft()

                for row_change, column_change in directions:
                    next_row = row + row_change
                    next_column = column + column_change

                    if (
                        next_row < 0
                        or next_row >= rows
                        or next_column < 0
                        or next_column >= columns
                        or grid[next_row][next_column] != 1
                    ):
                        continue

                    # The neighboring fresh fruit becomes rotten.
                    grid[next_row][next_column] = 2
                    fresh_fruit -= 1
                    queue.append((next_row, next_column))

            minutes += 1

        return minutes if fresh_fruit == 0 else -1