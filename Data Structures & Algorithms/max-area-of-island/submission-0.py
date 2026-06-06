from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        max_area = 0

        def dfs(row: int, column: int) -> int:
            if (
                row < 0
                or row >= rows
                or column < 0
                or column >= columns
                or grid[row][column] == 0
            ):
                return 0

            grid[row][column] = 0

            return (
                1
                + dfs(row + 1, column)
                + dfs(row - 1, column)
                + dfs(row, column + 1)
                + dfs(row, column - 1)
            )

        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == 1:
                    max_area = max(max_area, dfs(row, column))

        return max_area