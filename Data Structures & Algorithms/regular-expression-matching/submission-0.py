"""
dp(i, j) means: does s[i:] match p[j:]

check if current characters match
first_match = i < len(s) and (p[j] == s[i] or p[j] == ".")

then there are two cases:

No * after the current pattern character
Both pointers must move forward:
first_match and dp(i + 1, j + 1)

There is a *
We have two choices:
Use the preceding character zero times, so skip x*
    technically 0 times is a valid choice, get out of jail free card
Use it at least once, so consume one character from s and keep the pattern pointer at x*
dp(i, j + 2) or (first_match and dp(i + 1, j))

Memoization prevents recalculating the same states.
"""

from functools import cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def dp(i: int, j: int) -> bool:
            if j == len(p):
                return i == len(s)

            first_match = (
                i < len(s)
                and (p[j] == s[i] or p[j] == ".")
            )

            if j + 1 < len(p) and p[j + 1] == "*":
                return dp(i, j + 2) or (
                    first_match and dp(i + 1, j)
                )

            return first_match and dp(i + 1, j + 1)

        return dp(0, 0)