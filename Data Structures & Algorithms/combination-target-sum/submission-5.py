class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        n = len(nums)

        ans = set()

        nums.sort()

        def dfs(index, lst, sm):
            if sm == target:
                ans.add(tuple(lst[:]))
            
            if sm > target:
                return
            
            if index == n:
                return

            # skip current number
            dfs(index+1, lst, sm)

            # use number and stay on the index
            lst.append(nums[index])
            dfs(index, lst, sm+nums[index])
            lst.pop()
        
        dfs(0, [], 0)

        ans = [list(a) for a in ans]

        return ans