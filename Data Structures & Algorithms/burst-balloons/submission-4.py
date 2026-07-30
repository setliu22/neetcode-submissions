class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # dp[i][j] = max coins from popping nums[i:j+1]
        n = len(nums)

        if n == 0:
            return 0

        dp = [[0] * n for _ in range(n)]

        # Interval size: 1 through n
        for length in range(1, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1

                outside_left = nums[left - 1] if left > 0 else 1
                outside_right = nums[right + 1] if right < n - 1 else 1

                for k in range(left, right + 1):
                    left_score = dp[left][k - 1] if k > left else 0
                    right_score = dp[k + 1][right] if k < right else 0

                    pop_k_last = outside_left * nums[k] * outside_right

                    dp[left][right] = max(
                        dp[left][right],
                        left_score + pop_k_last + right_score
                    )

        return dp[0][n - 1]