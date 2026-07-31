class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # dp[i][j] is True if we can match the s[:i] with p[:j]
        # dp[0][0] is True
        # First row is false
        # First column is false
        # Maybe need to use diagonals

        n = len(s)
        m = len(p)

        # incorrect dimensions
        dp = [[False] * (m+1) for _ in range(n+1)]

        dp[0][0] = True

        # possible to match empty string "" b*b*b*

        for j in range(2, m+1): # starts at 1, first place an * could be
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]
        
        print(dp)

        # first column always false besides 0 0

        for i in range(1, n+1):
            for j in range(1, m+1):
                if s[i-1] == p[j-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                
                elif p[j-1] == '*':
                    # use zero of PRECEEDING (don't have to use)
                    dp[i][j] = dp[i][j-2]
                    # use up one or more if there is a match
                    if p[j-2] == s[i-1] or p[j-2] == '.':
                        # don't more the j pointer
                        dp[i][j] = dp[i][j] or dp[i-1][j]

        return dp[-1][-1]

