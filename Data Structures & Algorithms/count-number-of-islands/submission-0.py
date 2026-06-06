from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        islands = 0

        def dfs(row: int, column: int) -> None:
            # Stop if the position is outside the board or is not land.
            if (
                row < 0
                or row >= rows
                or column < 0
                or column >= columns
                or grid[row][column] == "0"
            ):
                return

            # Mark this land cell as visited.
            grid[row][column] = "0"

            # Visit all connected land cells.
            dfs(row + 1, column)
            dfs(row - 1, column)
            dfs(row, column + 1)
            dfs(row, column - 1)

        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == "1":
                    islands += 1
                    dfs(row, column)

        return islands