"""
just store for position i all possible ways, the way you get it is either take the stored value from i-1 and include the single digit, or go two back and add the two digits, but never add a leading 0

if two digits just make sure less than 26
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        dp = [0] * (n + 1)

        # One way to decode an empty string:
        # choose nothing.
        dp[0] = 1

        # First character can only be decoded if it is not zero.
        dp[1] = 0 if s[0] == "0" else 1

        for i in range(2, n + 1):
            one_digit = s[i - 1]

            if one_digit != "0":
                dp[i] += dp[i - 1]

            two_digits = int(s[i - 2:i])

            if 10 <= two_digits <= 26:
                dp[i] += dp[i - 2]

        return dp[n]