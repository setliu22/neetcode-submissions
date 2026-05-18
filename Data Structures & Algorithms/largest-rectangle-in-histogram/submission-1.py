# The stack is kept in increasing height order because of the construction rules.
# Before pushing a new height h, we remove everything taller than it
# "knows" which is better between 5 and 6 because survival bias, if you had 5, 6, then 2
# the 6's existence adds to the 5's rectangle, you didn't pop it at 6

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # stores pairs: (start_index, height)
        max_area = 0

        for i, h in enumerate(heights):
            start = i

            # Current bar is shorter, so taller bars must end before i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index

            stack.append((start, h))

        n = len(heights)

        # Anything left in stack extends to the end
        for index, height in stack:
            max_area = max(max_area, height * (n - index))

        return max_area