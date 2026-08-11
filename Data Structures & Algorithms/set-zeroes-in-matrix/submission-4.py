class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # set all initial 0's equal to *
        # then update rows, cols
        # then convert back

        n = len(matrix)
        m = len(matrix[0])

        # O(1) space

        first_col_zero = any(matrix[i][0] == 0 for i in range(n))
        first_row_zero = any(matrix[0][j] == 0 for j in range(m))

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, n):
            if matrix[i][0] == 0:
                for j in range(m):
                    matrix[i][j] = 0
        
        for j in range(1, m):
            if matrix[0][j] == 0:
                for i in range(n):
                    matrix[i][j] = 0
        
        if first_col_zero:
            for i in range(n):
                matrix[i][0] = 0
        
        if first_row_zero:
            for j in range(m):
                matrix[0][j] = 0
        