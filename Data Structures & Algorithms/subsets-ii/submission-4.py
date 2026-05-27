# Instead of using used, we use start

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        path = []

        # or you can do it like this
        res.append([])

        def backtrack(start):

            for i in range(start, len(nums)):
                # skip duplicates at same loop level, allow [1, 1]
                # if i > start to make sure we can actually run the command
                if i > start and nums[i] == nums[i - 1]:
                    continue

                path.append(nums[i])
                res.append(path.copy())
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return res