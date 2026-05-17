# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.best = float("-inf")

        def dfs(node):
            if not node:
                return 0

            # Best path sum going downward from the left child
            left_gain = max(dfs(node.left), 0)

            # Best path sum going downward from the right child
            right_gain = max(dfs(node.right), 0)

            # Best path where this node is the highest point
            current_path = node.val + left_gain + right_gain

            # Update global answer
            self.best = max(self.best, current_path)

            # Return the best single path upward
            return node.val + max(left_gain, right_gain)

        dfs(root)
        return self.best