class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        # build the trie

        trie = {}

        def insert(word):
            n = len(word)
            curr = trie

            for index in range(n):
                char = word[index]

                if index == n - 1:
                    char += '*'
                
                if char not in curr:
                    curr[char] = {}
                
                curr = curr[char]
        
        for word in words:
            insert(word)

        n = len(board)
        m = len(board[0])
        
        z = len(word)

        char = word[0]

        ans = set()

        def dfs(curr, currStr, i, j):
            char = board[i][j]
            if char not in curr and char + '*' not in curr:
                return
            if char + '*' in curr:
                ans.add(currStr + char)
            if char in curr:
                if i-1 > -1 and (i-1, j) not in visited:
                    visited.add((i-1, j))
                    dfs(curr[char], currStr + char, i-1, j)
                    visited.remove((i-1, j))
                if j-1 > -1 and (i, j-1) not in visited:
                    visited.add((i, j-1))
                    dfs(curr[char], currStr + char, i, j-1)
                    visited.remove((i, j-1))
                if i+1 < n and (i+1, j) not in visited:
                    visited.add((i+1, j))
                    dfs(curr[char], currStr + char, i+1, j)
                    visited.remove((i+1, j))
                if j+1 < m and (i, j+1) not in visited:
                    visited.add((i, j+1))
                    dfs(curr[char], currStr + char, i, j+1)
                    visited.remove((i, j+1))

        for i in range(n):
            for j in range(m):
                visited = {(i, j)}
                dfs(trie, "", i, j)
        
        return list(ans)