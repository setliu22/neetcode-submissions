"""
can we sum to 5
The two subsets must have equal sum, not an equal number of elements.
"""

class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2
        possible = {0}

        for num in nums:
            new_possible = possible.copy()

            for current_sum in possible:
                new_possible.add(current_sum + num)

            possible = new_possible

        return target in possible