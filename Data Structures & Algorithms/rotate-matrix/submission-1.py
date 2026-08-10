class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # everything below 1, 1, 2, 2, 3, 3

        n = len(matrix)

        for col in range(n):
            for row in range(col + 1, n):
                matrix[row][col], matrix[col][row] = \
                matrix[col][row], matrix[row][col]

        for row in range(n):
            matrix[row].reverse()