class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [1] * len(nums)

        # scan dp's before it, only take it and add to the 1 there if nums[j] < nums[i]

        for i in range(n):
            # i is the current index we are testing

            # also keep track of previous best dp value, put that there if you're not larger than previous values
            currMax = 0

            for j in range(i-1, -1, -1):
                # strictly increasing
                if nums[j] < nums[i] and dp[j] > currMax:
                    currMax = dp[j]
                    # don't break yet you could see something better

            dp[i] += currMax  
        
        print(dp)
        
        return max(dp)



        