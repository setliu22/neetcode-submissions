"""
dp[left][right] = (
    s[left] == s[right]
    and dp[left + 1][right - 1]
)

For substrings of length 1 or 2, there may not be a meaningful inside substring, so we handle them directly.

center expansion code:

class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        def expand(left, right):
            nonlocal count

            while (
                left >= 0
                and right < len(s)
                and s[left] == s[right]
            ):
                count += 1
                left -= 1
                right += 1

        for i in range(len(s)):
            expand(i, i)       # odd-length palindromes
            expand(i, i + 1)   # even-length palindromes

        return count

"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = 0

        for length in range(1, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1

                outside_matches = s[left] == s[right]

                if length <= 2:
                    inside_is_palindrome = True
                else:
                    inside_is_palindrome = dp[left + 1][right - 1]

                if outside_matches and inside_is_palindrome:
                    dp[left][right] = True
                    count += 1

        return count