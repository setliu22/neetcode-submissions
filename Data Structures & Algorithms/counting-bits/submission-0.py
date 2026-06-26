"""
The only issue is efficiency. For each number, you repeatedly remove one 1 bit, so the total time is roughly:

O(n log n)

The dynamic programming solution avoids recounting bits from scratch:

bits[i] = bits[i // 2] + i % 2

It uses an answer already computed for a smaller number, making the total time:

O(n)

Dynamic programming here just means:

Save answers for smaller numbers, then build larger answers from them.

For each number i, look at i // 2. In binary, dividing by 2 removes the last bit.

Example:

13 = 1101
6  = 110

So 13 contains all the 1 bits of 6, plus its final bit:

1101
110 + final bit 1

That gives:

bits[13] = bits[6] + 1

The final bit is found with i % 2:

bits[i] = bits[i // 2] + (i % 2)
Small table
i    binary    bits[i // 2]    final bit    answer
0    0                                      0
1    1         bits[0] = 0     1            1
2    10        bits[1] = 1     0            1
3    11        bits[1] = 1     1            2
4    100       bits[2] = 1     0            1
5    101       bits[2] = 1     1            2
6    110       bits[3] = 2     0            2
7    111       bits[3] = 2     1            3
"""

class Solution:
    def countBits(self, n: int) -> List[int]:
        bits = [0] * (n + 1)

        for i in range(1, n + 1):
            bits[i] = bits[i // 2] + (i % 2)

        return bits