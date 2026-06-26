"""
Binary addition has two parts:

a ^ b

calculates the sum without carrying.

(a & b) << 1

calculates which bits need to be carried left.

Then repeat until there is no carry.

Example: 4 + 7
4 = 0100
7 = 0111

First round:

sum without carry: 0100 XOR 0111 = 0011
carry:             0100 AND 0111 = 0100
carry shifted:                         1000

Now add 0011 and 1000:

0011 XOR 1000 = 1011 = 11
carry = 0

Answer: 11.
"""

class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while b != 0:
            partial_sum = (a ^ b) & mask
            carry = ((a & b) << 1) & mask

            a = partial_sum
            b = carry

        # Convert from unsigned 32-bit form back to Python negative integer
        return a if a <= max_int else ~(a ^ mask)
        