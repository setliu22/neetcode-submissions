"""
With two pointers, you sort first, then move left and right inward depending on whether the sum is too small or too large.

Sum equals 0: record it, then move BOTH inward.

or add tuples:

For each number, use a seen set to find two other numbers that complete zero, then add the sorted triplet as a tuple to a result set so duplicates are removed.

seen just means “numbers I already passed.”

Example: [-1, 0, 1]

Fix -1, then scan the rest:

At 0, you need 1, but you have not passed 1 yet. Add 0 to seen.
At 1, you need 0. 0 is in seen, so you found [-1, 0, 1].

you reset seen every time you choose a new fixed number.

n passes for n things, O(n^2)
"""

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()

        for i in range(len(nums)):
            seen = set()

            for j in range(i + 1, len(nums)):
                third = -nums[i] - nums[j]

                if third in seen:
                    result.add(tuple(sorted((nums[i], nums[j], third))))

                seen.add(nums[j])

        return [list(triplet) for triplet in result]