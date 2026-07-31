# dp solution take O(n) space, dp[i] is maximum subarray ending at index i

# either continue old subarray or start a new one

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        

        currSum = nums[0]

        maxAns = nums[0]

        for i in range(1, len(nums)):
            number = nums[i]

            # has to be best sum ending at that index
            # you can't skip to get the two

            # start fresh
            if number + currSum < number:
                currSum = number
            else:
                currSum = number+currSum
            
            maxAns = max(maxAns, currSum)
            print(currSum)
        
        return maxAns