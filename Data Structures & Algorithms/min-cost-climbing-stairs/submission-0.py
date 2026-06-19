# now it is not how many different ways to reach position i but instead cheapest total cost to reach position i

"""
# Min Cost Climbing Stairs
dp[i] = min(
    dp[i - 1] + cost[i - 1],
    dp[i - 2] + cost[i - 2]
)
cost [i] is the cost you pay when you leave the stair
"""
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)

        # dp[i] = minimum cost needed to reach position i
        # Position n represents the top.
        dp = [0] * (n + 1)

        # We can start at index 0 or index 1 for free.
        dp[0] = 0
        dp[1] = 0

        for i in range(2, n + 1):
            one_step = dp[i - 1] + cost[i - 1]
            two_steps = dp[i - 2] + cost[i - 2]

            dp[i] = min(one_step, two_steps)

        return dp[n]