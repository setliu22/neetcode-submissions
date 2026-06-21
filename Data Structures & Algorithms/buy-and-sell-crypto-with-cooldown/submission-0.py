"""
dp(day, can_buy) as the maximum profit possible starting from day.

the word max ineherently means the value is the same no matter how you reach there

if not holding
Skip today
Buy today

skip = dp(day + 1, True)
buy = -prices[day] + dp(day + 1, False)

if holding
Keep holding
Sell today
After selling, we go to day + 2 because the following day is the cooldown day.

hold = dp(day + 1, False)
sell = prices[day] + dp(day + 2, True)
"""

from functools import cache
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @cache
        def dp(day: int, can_buy: bool) -> int:
            if day >= n:
                return 0

            if can_buy:
                skip = dp(day + 1, True)
                buy = -prices[day] + dp(day + 1, False)

                return max(skip, buy)

            hold = dp(day + 1, False)
            sell = prices[day] + dp(day + 2, True)

            return max(hold, sell)

        return dp(0, True)   