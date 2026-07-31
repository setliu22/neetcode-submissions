import heapq

class Solution:
    def jump(self, nums: List[int]) -> int:
        # always try furthest jumps first
        # make visited set
        n = len(nums)

        if n == 1:
            return 0

        # last level furthest to the next level furthest is what you still have to explore
        # when you can reach the last index, return

        jumps = 0
        left = 0
        right = 0
        while True: # there is always an answer
        # since there's always an answer just assume start of next interval is previous furthest+1
            nextRight = 0
            for i in range(left, right+1):
                nextRight = max(nextRight, i+nums[i])

                if nextRight >= n-1:
                    return jumps+1
            
            jumps += 1

            left = right+1
            right = nextRight
            