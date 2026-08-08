from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # when it gets in the window it destroys all the smaller stuff ahead of it
        # a smaller added after it can still be the max
        # give it a time or something so you know when to pop it from the top

        ans = []

        queue = deque()

        for index, item in enumerate(nums):
            if queue:
                if queue[0][1] == index:
                    queue.popleft()
                while queue and queue[-1][0] <= item:
                    queue.pop()
                queue.append((item, index + k))
            
            else:
                queue.append((item, index + k))
            
            if index >= k - 1:
                ans.append(queue[0][0])
        
        return ans