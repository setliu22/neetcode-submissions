"""
cur.append(number)   # choose the number
dfs(...)             # explore what happens
cur.pop()            # undo the choice

track start index and total

and sort list cuz otherwise 299992 you gotta go back and look for prior 2
"""

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Sort so duplicate numbers are next to each other
        candidates.sort()

        # Final answers go here
        res = []

        # Current combination we are building
        cur = []

        def dfs(start, total):
            # If current combination adds to target, save a copy
            if total == target:
                res.append(cur.copy())
                return

            # If current sum is too big, stop this path
            if total > target:
                return

            # Try every possible next number
            for i in range(start, len(candidates)):

                # Skip duplicate numbers at the same level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Choose candidates[i]
                cur.append(candidates[i])

                # Move to i + 1 because each number can only be used once
                dfs(i + 1, total + candidates[i])

                # Undo the choice so we can try another number
                cur.pop()

        # Start with no numbers chosen and total 0
        dfs(0, 0)

        return res