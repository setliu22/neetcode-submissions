from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        columns = len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(row: int, column: int, visited: set) -> None:
            visited.add((row, column))

            directions = [
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1),
            ]

            for row_change, column_change in directions:
                next_row = row + row_change
                next_column = column + column_change

                if (
                    next_row < 0
                    or next_row >= rows
                    or next_column < 0
                    or next_column >= columns
                    or (next_row, next_column) in visited
                    or heights[next_row][next_column] < heights[row][column]
                ):
                    continue

                dfs(next_row, next_column, visited)

        # Pacific touches the top row and left column.
        for column in range(columns):
            dfs(0, column, pacific)

        for row in range(rows):
            dfs(row, 0, pacific)

        # Atlantic touches the bottom row and right column.
        for column in range(columns):
            dfs(rows - 1, column, atlantic)

        for row in range(rows):
            dfs(row, columns - 1, atlantic)

        result = []

        for row in range(rows):
            for column in range(columns):
                if (row, column) in pacific and (row, column) in atlantic:
                    result.append([row, column])

        return result