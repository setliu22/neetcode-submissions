"""
This operation removes the lowest 1 bit:

n = n & (n - 1)

Example:

n       = 101100
n - 1   = 101011
----------------
n & n-1 = 101000

One 1 disappeared.

So repeatedly remove one 1 bit and count how many times you can do it before n becomes 0.
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n:
            n &= n - 1
            count += 1

        return count