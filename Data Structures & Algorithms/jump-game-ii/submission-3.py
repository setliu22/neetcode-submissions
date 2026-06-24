"""

nums = [2, 3, 1, 1, 4]

0 jumps: index 0

1 jump:  indices 1, 2

2 jumps: indices 3, 4

current_end is the end of the current level
farthest is the end of the next level
i scans nodes inside the current level
jumps counts how many levels have been entered

i = 0  → count jump 1
i = 1  → do not count yet
i = 2  → finished checking everything reachable with jump 1
         now count jump 2

if i == current_end:
    jumps += 1
    current_end = farthest

current_end must remain fixed so we know when we are done
farthest can update

by the way, you don't make the exact jump. they just give you the limit
so if 3 you can jump 1, 2, 3
"""

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if i == current_end:
                jumps += 1
                current_end = farthest

        return jumps