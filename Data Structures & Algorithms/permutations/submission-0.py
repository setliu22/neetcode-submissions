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

            for i in range(len(nums)):
                if len(path) == len(nums):
                    res.append(path[:])
                    return

                if used[i]:
                    continue

                path.append(nums[i])
                used[i] = True

                backtrack()

                path.pop()
                used[i] = False

        backtrack()
        return res