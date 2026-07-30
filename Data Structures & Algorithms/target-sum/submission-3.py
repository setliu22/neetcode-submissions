class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # same thing, just go through item by item

        # 0 still has 1 way
        dp = {0: 1}

        for num in nums:
            # temp dict to avoid infinite calls while looping through dict
            temp_dp = {}

            for key, value in dp.items():
                if key+num not in temp_dp:
                    temp_dp[key+num] = dp[key]
                else:
                    temp_dp[key+num] += dp[key]

                if key-num not in temp_dp:
                    temp_dp[key-num] = dp[key]
                else:
                    temp_dp[key-num] += dp[key] 
            
            dp = temp_dp
            print(dp)

        return 0 if target not in dp else dp[target]