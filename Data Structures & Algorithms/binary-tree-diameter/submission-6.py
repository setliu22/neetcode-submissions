class Solution:
    def depth(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        return 1 + max(self.depth(node.left), self.depth(node.right))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        leftDepth = self.depth(root.left)
        rightDepth = self.depth(root.right)

        value = leftDepth + rightDepth
        value = max(value, self.diameterOfBinaryTree(root.left))
        value = max(value, self.diameterOfBinaryTree(root.right))

        return value