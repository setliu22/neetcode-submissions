"""
Solution: XOR

Use the bitwise XOR operator ^.

XOR has three useful properties:

a ^ a = 0
a ^ 0 = a
order does not matter

So every duplicate pair cancels out.

7 ^ 6 ^ 6 ^ 7 ^ 8
= (7 ^ 7) ^ (6 ^ 6) ^ 8
= 0 ^ 0 ^ 8
= 8
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0

        for num in nums:
            result ^= num

        return result