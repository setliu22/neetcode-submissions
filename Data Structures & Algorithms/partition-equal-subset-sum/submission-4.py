class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # you need to see if you can make total/2

        if sum(nums) % 2 != 0:
            return False

        # another exception is a number being larger than the half
        
        if nums[-1] > (sum(nums)/2):
            return False

        n = int(sum(nums)/2)

        dp = [False] * (n+1)

        dp[0] = True

        # process each element, if you CAN make n/2 with some elements the other elements must add up to n/2

        for num in nums:
            for j in range(n, num-1, -1):
                # keep dp true if it's true
                dp[j] = dp[j] or dp[j-num]

        return dp[-1]

