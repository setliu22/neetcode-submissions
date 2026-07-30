class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        dp with the choice to skip word or not

        process character by character (no infinite a's, 3 a's)
        
        dp[i] represents the number of ways to make s[:i]

        dp[0] is 1

        as you process each character, dp[i] goes up by 1 if dp[i-1] and
        newest character equals t[i-1]

        process characters in order this way order matters (direct subsequence  
        thing)
        """

        n = len(t)

        if len(s) < len(t):
            return 0
    
        dp = [0] * (n+1)

        dp[0] = 1

        for char in s:
            for i in range(n-1, -1, -1):
                # go in reverse order cuz you can't use a b twice
                if char == t[i] and dp[i] > 0:
                    dp[i+1] += dp[i]
        
        print(dp)
        
        return dp[-1]

        