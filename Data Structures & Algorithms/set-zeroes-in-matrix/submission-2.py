class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # set all initial 0's equal to *
        # then update rows, cols
        # then convert back

        n = len(matrix)
        m = len(matrix[0])

        # O(1) space

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    matrix[i][j] = '*'

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '*':
                    # don't overwrite *
                    for ii in range(n):
                        if matrix[ii][j] != '*':
                            matrix[ii][j] = 0
                    for jj in range(m):
                        if matrix[i][jj] != '*':
                            matrix[i][jj] = 0

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '*':
                    matrix[i][j] = 0


        