from collections import deque
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        rows = len(board)
        columns = len(board[0])
        queue = deque()

        def add_if_border_o(row: int, column: int) -> None:
            if board[row][column] == "O":
                board[row][column] = "S"
                queue.append((row, column))

        # Add every border "O" to the queue.
        for column in range(columns):
            add_if_border_o(0, column)
            add_if_border_o(rows - 1, column)

        for row in range(rows):
            add_if_border_o(row, 0)
            add_if_border_o(row, columns - 1)

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
        ]

        # Mark every "O" connected to a border as safe.
        while queue:
            row, column = queue.popleft()

            for row_change, column_change in directions:
                next_row = row + row_change
                next_column = column + column_change

                if (
                    0 <= next_row < rows
                    and 0 <= next_column < columns
                    and board[next_row][next_column] == "O"
                ):
                    board[next_row][next_column] = "S"
                    queue.append((next_row, next_column))

        # Capture enclosed regions and restore safe cells.
        for row in range(rows):
            for column in range(columns):
                if board[row][column] == "O":
                    board[row][column] = "X"
                elif board[row][column] == "S":
                    board[row][column] = "O"