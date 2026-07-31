class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # dp[i][j] represents the highest possible SCORE for nums[i:j+1]
        # 1's at the end
        # return dp[0][n-1]

        n = len(nums)
        
        dp = [[0] * n for _ in range(n)]

        # base case: dp[i][i] = nums[i]
        for i in range(n):
            leftSide = nums[i-1] if i > 0 else 1
            rightSide = nums[i+1] if i < n-1 else 1
            dp[i][i] = leftSide * nums[i] * rightSide
        
        # loop through everything else
        # start with smallest lengths, go to larger lengths

        for length in range(1, n): # since +1, [i][i+1] is length 2, last length is n-1
            for start in range(0, n-length): # last length is n-1, 0, 1
                # once we know start we should concretely put the end index somewhere
                end = start+length # at end ending index should be n-1

                # get outer left and outer right
                outer_left = nums[start-1] if start > 0 else 1
                outer_right = nums[end+1] if end < n-1 else 1

                # update dp using max directly
                for k in range(start, end+1):
                    leftScore = dp[start][k-1] if k > start else 0
                    rightScore = dp[k+1][end] if k < end else 0
                    kScore = nums[k] * outer_left * outer_right

                    dp[start][end] = max(dp[start][end], leftScore + rightScore + kScore)
        
        return dp[0][n-1]
