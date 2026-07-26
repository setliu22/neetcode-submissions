class Solution:
    def solve(self, board: List[List[str]]) -> None:

        def labeler(i, j):
            board[i][j] = "P"
            if i-1 > -1 and board[i-1][j] == "O":
                labeler(i-1, j)
            if i+1 < len(board) and board[i+1][j] == "O":
                labeler(i+1, j)
            if j-1 > -1 and board[i][j-1] == "O": 
                labeler(i, j-1)
            if j+1 < len(board[0]) and board[i][j+1] == "O":
                labeler(i, j+1)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and (i == 0 or i == len(board)-1 or j == 0 or j == len(board[0])-1):
                    labeler(i, j)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "P":
                    board[i][j] = "O"
        
        return