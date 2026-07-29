class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # store an array with smallest too in case negative numbers

        n = len(nums)

        dpMin = [1] * n
        dpMax = [1] * n

        dpMin[0] = nums[0]
        dpMax[0] = nums[0]

        for i in range(1, n):
            # previous values
            smallNum = nums[i] * dpMin[i-1]
            bigNum = nums[i] * dpMax[i-1]

            curr_small = min(smallNum, bigNum)
            curr_large = max(smallNum, bigNum) 
            # or just start fresh without multiplying by previous numbers

            curr_small = min(curr_small, nums[i])
            curr_large = max(curr_large, nums[i])

            dpMin[i] = curr_small
            dpMax[i] = curr_large
        
        return max(dpMax)


