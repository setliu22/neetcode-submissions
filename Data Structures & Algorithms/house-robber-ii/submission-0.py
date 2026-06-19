"""
just do same method once do on one index then move one to the left or right and do again

Because the houses form a circle, the first and last houses are adjacent. So they cannot both be included.
"""

class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_line(houses):
            previous_two = 0
            previous_one = 0

            for money in houses:
                rob_current = previous_two + money
                skip_current = previous_one

                current = max(rob_current, skip_current)

                previous_two = previous_one
                previous_one = current

            return previous_one

        exclude_last = rob_line(nums[:-1])
        exclude_first = rob_line(nums[1:])

        return max(exclude_last, exclude_first)