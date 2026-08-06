class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        stack = []

        currMax = 0

        ans = 0

        for index, item in enumerate(heights):
            if not stack:
                stack.append((index, item))
            elif item < stack[-1][1]:
                # pop everything that it's shorter than
                while stack and item < stack[-1][1]:
                    old_index, old_item = stack.pop()
                    ans = max(ans, (index - old_index) * (old_item))
                stack.append((old_index, item))
            else:
                stack.append((index, item))
        
        # pop remaining things in the stack

        while stack:
            index, item = stack.pop()
            ans = max(ans, (n - index) * item)

        return ans
