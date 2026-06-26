"""
The two if checks matter because eventually there may be only one row or one column left. Without checking, those values could be added twice.

Maintain four boundaries around the unvisited area:

top, bottom, left, right

For each layer:

Read the top row from left to right.
Read the right column from top to bottom.
Read the bottom row from right to left.
Read the left column from bottom to top.
Move all four boundaries inward.
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # Top row
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1

            # Right column
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1

            # Bottom row, if one remains
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1

            # Left column, if one remains
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1

        return result