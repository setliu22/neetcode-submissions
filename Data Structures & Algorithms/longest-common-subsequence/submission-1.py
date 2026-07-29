class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 2d DP problem
        # dp[i][j] is longest between text1[:i] and text2[:j]
    
        n = len(text1)
        m = len(text2)
        dp = [[0] * (m+1) for _ in range(n+1)]

        print(dp)

        for i in range(n+1):
            print(i)
            dp[i][0] = 0
    
        for i in range(m+1):
            dp[0][i] = 0

        # cat
        # cattt

        for i in range(1, n+1):
            for j in range(1, m+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    # you know the chars are unrelated
                    # but they could match an earlier one
                    # one char should be skipped, we should make sure to keep useful one
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]