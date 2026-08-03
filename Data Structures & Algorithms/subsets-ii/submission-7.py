class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set()

        # just include or exclude with extra set restriction

        n = len(nums)

        def dfs(index, lst):
            if index == n:
                if lst != []:
                    ans.add(tuple(sorted(lst)))
                else:
                    ans.add(tuple(lst.copy()))
                return
                
            # skip
            dfs(index+1, lst)

            # add
            lst.append(nums[index])
            dfs(index+1, lst)
            lst.pop()
            

        dfs(0, [])

        ans = [list(a) for a in ans]

        return ans
