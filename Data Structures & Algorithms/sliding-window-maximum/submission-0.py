from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()   # stores indexes of useful max candidates
        res = []

        for right in range(len(nums)):
            # Remove smaller values from the back
            # They can never be the max while nums[right] is in the window
            while q and nums[q[-1]] < nums[right]:
                q.pop()

            # Add current index
            q.append(right)

            # Remove indexes that are outside the current window
            # Deque doesn't always match up with window exactly, the index might already be gone from deque
            if q[0] <= right - k:
                q.popleft()

            # Start recording answers once the first full window is formed
            if right >= k - 1:
                res.append(nums[q[0]])

        return res