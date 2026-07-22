# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        self.ans = True

        def dfs(node):
            if node is None:
                return 0

            leftSide = dfs(node.left)
            rightSide = dfs(node.right)

            if abs(leftSide - rightSide) > 1:
                self.ans = False

            return 1+max(dfs(node.left), dfs(node.right))

        dfs(root)

        return self.ans