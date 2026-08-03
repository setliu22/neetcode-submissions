class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        results = []

        def dfs(index, lst):
            if index == n:
                results.append(lst[:])
                return
            
            dfs(index+1, lst)

            lst.append(nums[index])

            dfs(index+1, lst)

            lst.pop()
        
        dfs(0, [])

        return results
        