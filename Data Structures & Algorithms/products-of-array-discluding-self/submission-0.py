class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prodleft = [1] * n
        prodright = [1] * n
        ans = [1] * n

        # prodleft[i] = product of everything to the left of i
        for i in range(1, n):
            prodleft[i] = prodleft[i - 1] * nums[i - 1]

        # prodright[i] = product of everything to the right of i
        for i in range(n - 2, -1, -1):
            prodright[i] = prodright[i + 1] * nums[i + 1]

        for i in range(n):
            ans[i] = prodleft[i] * prodright[i]

        return ans