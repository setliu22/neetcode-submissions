"""
Let dp[left][right] be the maximum coins from bursting all balloons strictly between left and right.

dp[left][right] = max(
    dp[left][k]
    + nums[left] * nums[k] * nums[right]
    + dp[k][right]
)

the formula assumes left and right are still present when k is burst last, they are not candidates for k

assume oob left/right is 1 

Yes. You enumerate every interval, try every possible last balloon k inside it, and reuse answers for the smaller left and right intervals.

The knobs are adjusted in this order:

Interval length, from small to large
Start boundary, from left to right
end boundary is a given based on interval length and start boundary
Try every possible k inside that interval

k requires knowledge of the intervals to the left and right of it which are shorter intervals
you would have known 1/3 and 2

So there are THREE CHOICES being enumerated:

Left and right boundaries
Which balloon k is last

That is why the time complexity is O(n³). Each dp[left][right] is computed once, but while computing it, you test every valid k.

length = 2:
    left = 0, right = 2
    left = 1, right = 3
    left = 2, right = 4

length = 3:
    left = 0, right = 3
    left = 1, right = 4

length = 4:
    left = 0, right = 4

So the algorithm solves small intervals first, then larger intervals.

Small intervals:
[0 ... 2]
    [1 ... 3]
        [2 ... 4]

Larger intervals:
[0 ..... 3]
    [1 ..... 4]

Complete interval:
[0 ......... 4]

Later, while calculating the full problem dp[0][4], one possibility is that k = 3 is burst last:

dp[0][3] + balloons[0] * balloons[3] * balloons[4] + dp[3][4]

We do not solve the balloons between 0 and 3 again. We simply look up:

dp[0][3]

from the table.
"""

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        balloons = [1] + nums + [1]
        n = len(balloons)

        dp = [[0] * n for _ in range(n)]

        # interval length
        for length in range(2, n):
            for left in range(n - length):
                right = left + length

                for k in range(left + 1, right):
                    coins = (
                        dp[left][k]
                        + balloons[left] * balloons[k] * balloons[right]
                        + dp[k][right]
                    )
                    dp[left][right] = max(dp[left][right], coins)

        return dp[0][n - 1]