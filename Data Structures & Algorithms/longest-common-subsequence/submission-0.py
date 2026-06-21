"""
case 1: match
include that character
dp[i][j] = 1 + dp[i - 1][j - 1]

case 2: don't match
ignore the current character from text1
or
ignore the current character from text2
dp[i][j] = max(
    dp[i - 1][j],
    dp[i][j - 1]
)

fill in zeros to start

       ""  c  r  a  b  t
""      0  0  0  0  0  0
c       0  1  1  1  1  1
a       0  1  1  2  2  2
t       0  1  1  2  2  3

the only work you need to do is a single character comparison 
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows = len(text1) + 1
        cols = len(text2) + 1

        dp = [[0] * cols for _ in range(rows)]

        for i in range(1, rows):
            for j in range(1, cols):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(
                        dp[i - 1][j],
                        dp[i][j - 1]
                    )

        return dp[-1][-1] 