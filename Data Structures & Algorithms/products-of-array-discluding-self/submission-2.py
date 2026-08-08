class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # calculate all prefix and suffix products
        # these are easy to calculate cuz you just reuse prev answer and multiply
        # rather than go 100 deep each time you just reuse a prev answer
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n
        
        prefix[0] = 1

        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        suffix[n-1] = 1

        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        
        ans = [prefix[i] * suffix[i] for i in range(n)]

        return ans