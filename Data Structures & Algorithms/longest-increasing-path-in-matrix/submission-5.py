class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # dp[r][c] is longest path starting at that index
        # you can reuse an answer you have already if you're smaller than that index

        # just start filling shi out

        n = len(matrix)
        m = len(matrix[0])

        # no need for 0 index stuff with strings s[:i]

        # initial values should be 1
        dp = [[1] * m for _ in range(n)]

        def dfs(i, j):
            # how to prevent going back and forth
            topSum = 0
            leftSum = 0
            botSum = 0
            rightSum = 0

            if i-1 > -1 and matrix[i-1][j] > matrix[i][j]:
                if dp[i-1][j] > 1:
                    topSum = dp[i-1][j]
                else:
                    topSum = dfs(i-1, j)
                    dp[i-1][j] = topSum
                
            if j-1 > -1 and matrix[i][j-1] > matrix[i][j]:
                if dp[i][j-1] > 1:
                    leftSum = dp[i][j-1]
                else:
                    leftSum = dfs(i, j-1)
                    dp[i][j-1] = leftSum

            if i+1 < n and matrix[i+1][j] > matrix[i][j]:
                if dp[i+1][j] > 1:
                    botSum = dp[i+1][j]
                else:
                    botSum = dfs(i+1, j)
                    dp[i+1][j] = botSum

            if j+1 < m and matrix[i][j+1] > matrix[i][j]:
                if dp[i][j+1] > 1:
                    rightSum = dp[i][j+1]
                else:
                    rightSum = dfs(i, j+1)
                    dp[i][j+1] = rightSum
            
            return 1+max(leftSum, rightSum, topSum, botSum)

        for i in range(n):
            for j in range(m):
                if dp[i][j] == 1:
                    dp[i][j] = dfs(i, j)


        maxval = 0

        print(dp)

        for i in range(n):
            for j in range(m):
                maxval = max(maxval, dp[i][j])

        return maxval
                