"""
dp[i][j] = minimum operations needed to turn
           word1[:i] into word2[:j]

           :i and :j are why it's i-1, j-1

dp[i][0] = i     # delete all i characters
dp[0][j] = j     # insert all j characters

if word1[i - 1] == word2[j - 1], dp[i][j] = dp[i - 1][j - 1]

if characters do not match,
dp[i - 1][j]       delete word1[i - 1]
dp[i][j - 1]       insert word2[j - 1]
dp[i - 1][j - 1]   replace word1[i - 1]

dp[i][j] = 1 + min(delete, insert, replace)

"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        rows = len(word1) + 1
        cols = len(word2) + 1

        dp = [[0] * cols for _ in range(rows)]

        # Convert word1[:i] into an empty string
        # This requires deleting i characters
        for i in range(rows):
            dp[i][0] = i

        # Convert an empty string into word2[:j]
        # This requires inserting j characters
        for j in range(cols):
            dp[0][j] = j

        for i in range(1, rows):
            for j in range(1, cols):
                if word1[i - 1] == word2[j - 1]:
                    #just reuse the last answer
                    #i-1 and j-1 since :i and :j
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    delete = dp[i - 1][j]
                    insert = dp[i][j - 1]
                    replace = dp[i - 1][j - 1]

                    dp[i][j] = 1 + min(delete, insert, replace)

        return dp[len(word1)][len(word2)]   