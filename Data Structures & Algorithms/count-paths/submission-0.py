"""
Backtracking enumerates every complete route individually.
DP counts all routes indirectly by combining previously computed counts.

ways[r][c] = ways[r - 1][c] + ways[r][c - 1]
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp[c] stores the number of ways to reach the current row's cell
        # in column c.
        dp = [1] * n

        for r in range(1, m):
            for c in range(1, n):
                dp[c] = dp[c] + dp[c - 1]

        return dp[n - 1]