# just add ways to get to step 2 steps before, ways to get to step 1 step before

class Solution:
    def climbStairs(self, n: int) -> int:
        ways = [0] * (n + 1)

        ways[1] = 1

        if n >= 2:
            ways[2] = 2

        for stair in range(3, n + 1):
            ways[stair] = ways[stair - 1] + ways[stair - 2]

        return ways[n]