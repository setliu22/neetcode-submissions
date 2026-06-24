"""
Index 0: farthest becomes 1
Index 1: farthest becomes 3
Index 2: farthest stays 3
Index 3: farthest stays 3
Index 4 is greater than 3, so index 4 is unreachable
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0

        for i, jump in enumerate(nums):
            if i > farthest:
                return False

            farthest = max(farthest, i + jump)

            if farthest >= len(nums) - 1:
                return True

        return True