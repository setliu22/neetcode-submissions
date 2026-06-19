"""
dp[i] = max(
    dp[i - 1],             # skip current house
    nums[i] + dp[i - 2]    # rob current house
)
"""

class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            skip_current = dp[i - 1]
            rob_current = nums[i] + dp[i - 2]

            dp[i] = max(skip_current, rob_current)

        return dp[-1]