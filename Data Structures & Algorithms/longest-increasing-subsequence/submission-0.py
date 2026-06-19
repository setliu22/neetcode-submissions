"""
start from the back

dp i is how long it can be after that index

work backwards

this way it automatically knows whether to choose between 7 and 3
and then add 1 and make that the 2 value
"""

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)

        # Every single number is an increasing subsequence of length 1.
        dp = [1] * n

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)