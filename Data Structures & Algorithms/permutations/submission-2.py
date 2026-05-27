"""
Every call to backtrack() starts its own for i in range(len(nums)) from the beginning.
So even when you are deep inside the recursion, the loop starts checking from index 0 again.

how we avoid repeats of work:
Call C tried i = 0
Call C tried i = 1
Call C tried i = 2

call A gonna try all the ones with 1 initially then do 2
call B and C follow similar testing logic that we didn't do except there's a checker to make sure we didn't do that one already

so the loop ensures we don't repeat things we've tried already
the list ensures we don't use things we've used already
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used = [False] * len(nums)

        def backtrack():

            #this can be anywhere but it's more efficient technically to put it outside
            # as long as return is before calling backtrack again so there is stoppage/no infinite calls
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