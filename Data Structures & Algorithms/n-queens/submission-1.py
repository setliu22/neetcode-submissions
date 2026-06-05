from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions: List[List[str]] = []

        board = [["."] * n for _ in range(n)]

        # Track positions that are already attacked.
        used_columns = set()
        used_diagonals = set()       # row - column
        used_anti_diagonals = set()  # row + column

        def backtrack(row: int) -> None:
            # Every row has received one valid queen.
            if row == n:
                solutions.append(["".join(current_row) for current_row in board])
                return

            for column in range(n):
                diagonal = row - column
                anti_diagonal = row + column

                # Skip placements that would cause an attack.
                if (
                    column in used_columns
                    or diagonal in used_diagonals
                    or anti_diagonal in used_anti_diagonals
                ):
                    continue

                # Choose: place a queen.
                board[row][column] = "Q"
                used_columns.add(column)
                used_diagonals.add(diagonal)
                used_anti_diagonals.add(anti_diagonal)

                # Explore the next row.
                backtrack(row + 1)

                # Undo the choice so another column can be tested.
                board[row][column] = "."
                used_columns.remove(column)
                used_diagonals.remove(diagonal)
                used_anti_diagonals.remove(anti_diagonal)

        backtrack(0)
        return solutions