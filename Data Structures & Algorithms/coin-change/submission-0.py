"""

every single combination has a "final coin" to reach a certain value

Use coin 1:
dp[9] + 1

Use coin 5:
dp[5] + 1 = 2

Use coin 10:
dp[0] + 1 = 1

each index just store least value

"""

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        impossible = amount + 1

        dp = [impossible] * (amount + 1)
        dp[0] = 0

        for current_amount in range(1, amount + 1):
            for coin in coins:
                if coin <= current_amount:
                    dp[current_amount] = min(
                        dp[current_amount],
                        dp[current_amount - coin] + 1
                    )

        return -1 if dp[amount] == impossible else dp[amount]