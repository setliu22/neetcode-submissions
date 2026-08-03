class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        n = len(nums)

        def dfs(index, lst):
            if index == n:
                ans.add(tuple(sorted(lst)))
                return

            # skip
            dfs(index + 1, lst)

            # include
            lst.append(nums[index])
            dfs(index + 1, lst)
            lst.pop()

        dfs(0, [])

        return [list(subset) for subset in ans]