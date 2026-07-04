"""
dp(i, j) means: does s[i:] match p[j:]
so dp(ZERO, ZERO) is the answer

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


if you want to cancel immediately, you can if you don't see a * after
Mismatch with no following *:
    return False immediately

Mismatch with a following *:
    skip x* and continue checking
"""

"""
def dp(i, j):
    # If there is no pattern remaining,
    # succeed only if there is also no string remaining.
    if j == len(p):
        return i == len(s)

    # Do the current characters match?
    first_match = (
        i < len(s)
        and (p[j] == s[i] or p[j] == ".")
    )

    # Current pattern piece is something like a*
    if j + 1 < len(p) and p[j + 1] == "*":
        return (
            dp(i, j + 2)                 # use a* zero times
            or
            (first_match and dp(i + 1, j))  # use a* once or more
        )

    # No star, so current characters must match.
    return first_match and dp(i + 1, j + 1)
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