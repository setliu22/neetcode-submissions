class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        used = [False] * n

        ans = []

        def dfs(lst):
            if len(lst) == n:
                ans.append(lst[:])
                return
        
            for i in range(n):
                if not used[i]:
                    lst.append(nums[i])
                    used[i] = True
                    dfs(lst)

                    lst.pop()
                    used[i] = False

        dfs([])

        return ans