class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # 1. Transpose
        for row in range(n):
            for col in range(row + 1, n):
                matrix[row][col], matrix[col][row] = (
                    matrix[col][row],
                    matrix[row][col]
                )

        # 2. Reverse each row
        for row in matrix:
            row.reverse()