class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # dp[i][j] if s1[:i], s2[:j] make s3[:i+j]
        # s[:i] corresponds to s[i-1]
        # so we need the +1 for the dp
        # the first instance of false means the whole thing is false


        n = len(s1)
        m = len(s2)

        if len(s3) != n+m:
            return False

        dp = [[False] * (m+1) for _ in range(n+1)]

        # base cases
        dp[0][0] = True

        # handle top row
        for i in range(1, m+1):
            dp[0][i] = dp[0][i-1] and (s2[i-1] == s3[i-1]) 

        # handle left column
        for i in range(1, n+1):
            dp[i][0] = dp[i-1][0] and (s1[i-1] == s3[i-1]) 

        for i in range(1, n+1):
            for j in range(1, m+1):
                # to take_s1 to be true, dp[i-1][j] must be true and s1[i-1] == s3[i+j-1]
                take_s1 = dp[i-1][j] and s1[i-1] == s3[i+j-1]

                take_s2 = dp[i][j-1] and s2[j-1] == s3[i+j-1]

                dp[i][j] = take_s1 or take_s2
        
        return dp[-1][-1]
