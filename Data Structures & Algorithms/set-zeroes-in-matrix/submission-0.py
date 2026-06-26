"""
space requirement: if you can't store the zeros somewhere

During the first pass, we do not zero the whole row and column. We only mark:

matrix[1][0] = 0
matrix[0][2] = 0

special code

Those two new zeros are just notes:

matrix[1][0] = 0 means zero row 1
matrix[0][2] = 0 means zero column 2

The crucial part is that the first pass scans only the inner matrix:

for r in range(1, rows):
    for c in range(1, cols):

        So it does not inspect the first row or first column, where we are writing the marker zeros. Therefore, those new zeros cannot create more markers.

Then, in the second pass, we use the markers:

"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])

        first_row_zero = any(matrix[0][c] == 0 for c in range(cols))
        first_col_zero = any(matrix[r][0] == 0 for r in range(rows))

        # Mark rows and columns that need to become zero
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        # Zero cells based on the markers
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # Handle the first row and first column
        if first_row_zero:
            for c in range(cols):
                matrix[0][c] = 0

        if first_col_zero:
            for r in range(rows):
                matrix[r][0] = 0
        