"""
It actually is dynamic programming. Kadane’s algorithm is just a space-optimized DP solution.

dp[i] = maximum subarray sum that ends exactly at index i

For nums[i], there are only two choices:

Start a new subarray at nums[i]
Extend the best subarray that ended at i - 1

dp[i] = max(nums[i], dp[i - 1] + nums[i])

But dp[i] only depends on dp[i - 1], so we do not need the whole array. We replace it with one variable that keeps getting its value updated using its previous value:
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        max_sum = nums[0]

        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum