class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        if n <= 1:
            return 0

        dpStock = [0] * n
        dpNone = [0] * n

        # Day 0
        dpStock[0] = -prices[0]
        dpNone[0] = 0

        # Day 1
        dpStock[1] = max(dpStock[0], -prices[1])
        dpNone[1] = max(dpNone[0], dpStock[0] + prices[1])

        # Day 2 onward
        for i in range(2, n):
            dpStock[i] = max(
                dpStock[i - 1],
                dpNone[i - 2] - prices[i]
            )

            dpNone[i] = max(
                dpNone[i - 1],
                dpStock[i - 1] + prices[i]
            )

        return dpNone[-1]