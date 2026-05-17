class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        leftside = self.maxDepth(root.left)
        rightside = self.maxDepth(root.right)

        return 1 + max(leftside, rightside)