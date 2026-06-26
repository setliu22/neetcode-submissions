"""
The sum of all numbers from 0 to n is:

n * (n + 1) // 2

Subtract the numbers that actually appear.
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected = n * (n + 1) // 2
        actual = sum(nums)

        return expected - actual