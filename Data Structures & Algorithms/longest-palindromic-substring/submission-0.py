"""
dp not really the optimal sol

dp[left][right] = (
    s[left] == s[right]
    and dp[left + 1][right - 1]
)

“Can I keep expanding outward while both characters match?” It is simpler than the DP version and uses constant extra space.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        # dp[left][right] tells us whether
        # s[left:right + 1] is a palindrome
        dp = [[False] * n for _ in range(n)]

        longest_start = 0
        longest_length = 1

        # Build shorter substrings before longer substrings
        for right in range(n):
            for left in range(right + 1):
                outer_chars_match = s[left] == s[right]
                inside_is_palindrome = (
                    right - left <= 2
                    or dp[left + 1][right - 1]
                )

                if outer_chars_match and inside_is_palindrome:
                    dp[left][right] = True

                    current_length = right - left + 1

                    if current_length > longest_length:
                        longest_start = left
                        longest_length = current_length

        return s[longest_start:longest_start + longest_length]