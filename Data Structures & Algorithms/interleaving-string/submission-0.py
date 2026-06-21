"""

We are just tracking two pointers:

(i, j)
i = how many characters we already took from s1
j = how many characters we already took from s2

The next position in s3 is automatically:

next position in the s3 we are generating is i+j

If the same (i, j) appears again, Python reuses the saved answer instead of recalculating it.

so if no we don't go down that path

if i == len(s1) and j == len(s2):
    return True

since the problem statement says i+j is length of s3

the only speedup we get from dp is when we know a path DOESNT work right
"""

from functools import cache


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        @cache
        def canFinish(i: int, j: int) -> bool:
            # Done: every character from s1 and s2 was used
            if i == len(s1) and j == len(s2):
                return True

            k = i + j

            # Take next character from s1
            if i < len(s1) and s1[i] == s3[k]:
                if canFinish(i + 1, j):
                    return True

            # Take next character from s2
            if j < len(s2) and s2[j] == s3[k]:
                if canFinish(i, j + 1):
                    return True

            return False

        return canFinish(0, 0)