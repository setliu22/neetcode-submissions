"""
Every call to backtrack() starts its own for i in range(len(nums)) from the beginning.
So even when you are deep inside the recursion, the loop starts checking from index 0 again.

"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used = [False] * len(nums)

        def backtrack():

            #this can be anywhere but it's more efficient technically to put it outside

            if len(path) == len(nums):
                res.append(path[:])
                return
                
            for i in range(len(nums)):
                if used[i]:
                    continue

                path.append(nums[i])
                used[i] = True

                backtrack()

                path.pop()
                used[i] = False

        backtrack()
        return res