class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        n = len(nums)

        ans = set()

        nums.sort()

        def dfs(index, lst):
            if sum(lst) == target:
                ans.add(tuple(lst[:]))
            
            if sum(lst) > target:
                return
            
            if index == n:
                return

            # skip current number
            dfs(index+1, lst)

            # use number and stay on the index
            lst.append(nums[index])
            dfs(index, lst)
            lst.pop()
        
        dfs(0, [])

        ans = [list(a) for a in ans]

        return ans