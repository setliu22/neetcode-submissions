"""
1. index: which number are we currently assigning?
2. total: what is the current sum?

dp(index, total) = (
    dp(index + 1, total + nums[index]) 
    +
    dp(index + 1, total - nums[index])


index 0: we are choosing a sign for the first number
total 0: our running total is currently 0

At every number, recursion first tries +, then -.

will return 0 ways if used all 3 didnt get there

this is just exploring all branches
)

caching helps you avoid going down a branch if you already did it

"""

from functools import cache
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def dp(index: int, total: int) -> int:
            # We assigned a sign to every number.
            if index == len(nums):
                return 1 if total == target else 0

            add = dp(index + 1, total + nums[index])
            subtract = dp(index + 1, total - nums[index])

            return add + subtract

        return dp(0, 0)