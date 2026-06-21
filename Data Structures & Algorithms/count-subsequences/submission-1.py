"""
Let:

dp[i][j]

represent the number of ways to form the first j characters of t using the first i characters of s.

For every character in s, there are two choices:

Skip s[i - 1]
Use s[i - 1] if it matches t[j - 1]

base case: dp[i][0] = 1

dp[i][j] = dp[i - 1][j]

if characters match: dp[i][j] += dp[i - 1][j - 1] ( add that too )

dp[2][1] counts the ways to get a c from the 2 characters

dp[3][2] = dp[2][2] + dp[2][1]
second is using the character

only first dp[2][2] if no match

1d solution
dp[j] = number of ways to build the first j characters of t


start       [1, 0, 0, 0]
after c     [1, 1, 0, 0]
after a     [1, 1, 1, 0]
after a     [1, 1, 2, 0]
after a     [1, 1, 3, 0]
after t     [1, 1, 3, 3]

process backwards so a doesn't match to aa

j = 2: dp[2] += dp[1]
       0 += 0

j = 1: dp[1] += dp[0]
       0 += 1

We read source characters left to right, but update the bookkeeping right to left so each source character is used at most once per subsequence.
110 not 112
"""

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j]

                if s[i - 1] == t[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]

        return dp[m][n]