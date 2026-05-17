class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for r in range(9):
            for c in range(9):
                num = board[r][c]

                if num == ".":
                    continue

                row_check = ("row", r, num)
                col_check = ("col", c, num)
                box_check = ("box", r // 3, c // 3, num)

                if row_check in seen:
                    return False

                if col_check in seen:
                    return False

                if box_check in seen:
                    return False

                seen.add(row_check)
                seen.add(col_check)
                seen.add(box_check)

        return True