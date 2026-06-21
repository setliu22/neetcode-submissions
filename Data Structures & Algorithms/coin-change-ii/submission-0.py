"""
dp[i][a]
Number of combinations that make amount a using the first i coin types.

dp[2][4] means:

How many ways can we make 4 using coins [1, 2]?

Because coins are unlimited, we stay on the same row
dp[i][a] = dp[i - 1][a] + dp[i][a - coin]
first one is do not use the coin (and only use earlier types), second is use it and stay on same row



"""

from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        # There is one way to make amount 0:
        # choose no coins.
        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(1, n + 1):
            coin = coins[i - 1]

            for current_amount in range(1, amount + 1):
                # Do not use this coin.
                dp[i][current_amount] = dp[i - 1][current_amount]

                # Use this coin.
                if current_amount >= coin:
                    dp[i][current_amount] += dp[i][current_amount - coin]

        return dp[n][amount]