"""

Step 1

Rightmost bit of n is 1.

n      = 1101
result = 0001

Remove that bit from n:

n = 0110
Step 2

Rightmost bit is now 0.

First move result left:

0001 → 0010

Then insert 0:

result = 0010
n = 0011
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0

        for _ in range(32):
            result = result << 1   # make room
            result += n & 1        # copy n's last bit
            n = n >> 1             # remove n's last bit

        return result