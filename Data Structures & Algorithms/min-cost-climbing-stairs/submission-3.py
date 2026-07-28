class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        if len(cost) <= 2:
            return min(cost)

        ans = [0] * (len(cost)+1)
        ans[0] = 0
        ans[1] = 0

        for i in range(2, len(cost)+1):
            ans[i] += min(ans[i-1]+cost[i-1], ans[i-2]+cost[i-2])

        print(ans)
        return ans[-1]