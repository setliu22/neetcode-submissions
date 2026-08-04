class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # just finding which column to place each in
        # combinations = backtracking

        """
        0 0
        1 1
        2 2 
        3 3

        3 0
        2 1
        1 2
        0 3
        """
        if n == 1:
            return [["Q"]]

        ans = []

        def diagonal(row, col):
            return row - col
        
        def antidiagonal(row, col):
            return row + col

        def dfs(row):
            if row == n:
                ans.append(lst[:])
                print(lst)
                return

            for col in range(n):
                if col not in columns and diagonal(row, col) not in diagonals and antidiagonal(row, col) not in antidiagonals:
                    diagonals.add(diagonal(row, col))
                    antidiagonals.add(antidiagonal(row, col))
                    columns.add(col)
                    lst.append(col)
                    dfs(row+1)
                    diagonals.remove(diagonal(row, col))
                    antidiagonals.remove(antidiagonal(row, col))
                    columns.remove(col)
                    lst.pop()
            
        def turn_to_output(output):
            print(output)

        for i in range(n): # place the queen in the top row
            columns = {i}
            lst = [i]
            diagonals = {-i}
            antidiagonals = {i}

            dfs(1)

        print(ans)

        for element in ans:
        # [1, 3, 0, 2]
            for i in range(n):
                index = element[i]
                str1 = ''
                for j in range(n):
                    if j != index:
                        str1 += '.'
                    else:
                        str1 += 'Q'
            
                element[i] = str1

        print(ans)
        return ans