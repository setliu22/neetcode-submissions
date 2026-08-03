class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # strings so no need to pop

        n = len(board)
        m = len(board[0])
        
        z = len(word)

        char = word[0]

        def dfs(index, i, j):
            if board[i][j] != word[index]:
                return False
            if index == z-1:
                return True
            if board[i][j] == word[index]:
                if i-1 > -1 and (i-1, j) not in visited:
                    visited.add((i-1, j))
                    if dfs(index+1, i-1, j):
                        return True
                    visited.remove((i-1, j))
                if j-1 > -1 and (i, j-1) not in visited:
                    visited.add((i, j-1))
                    if dfs(index+1, i, j-1):
                        return True
                    visited.remove((i, j-1))
                if i+1 < n and (i+1, j) not in visited:
                    visited.add((i+1, j))
                    if dfs(index+1, i+1, j):
                        return True
                    visited.remove((i+1, j))
                if j+1 < m and (i, j+1) not in visited:
                    visited.add((i, j+1))
                    if dfs(index+1, i, j+1):
                        return True
                    visited.remove((i, j+1))
                return False

        for i in range(n):
            for j in range(m):
                if board[i][j] == char:
                    visited = {(i, j)}
                    if dfs(0, i, j):
                        return True
        
        return False