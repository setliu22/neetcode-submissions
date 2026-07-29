class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # if there is a block above, add # of ways to get to that block
        # if there is a block to the left, add # of ways to get to that block

        dp = [[0] * n for _ in range(m)]

        # base cases
        for i in range(m):
            dp[i][0] = 1

        for i in range(n):
            dp[0][i] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]
