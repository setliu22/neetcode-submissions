"""
The sum of all numbers from 0 to n is:

n * (n + 1) // 2

Subtract the numbers that actually appear.

XOR every number in nums with every number from 0 through n.

Every number that appears in both groups cancels out. The only number left is the missing one.
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)

        for i, num in enumerate(nums):
            result ^= i
            result ^= num

        return result