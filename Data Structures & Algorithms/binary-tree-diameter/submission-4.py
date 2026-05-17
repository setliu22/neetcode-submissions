class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def depth(node):
            if not node:
                return 0
            return 1 + max(depth(node.left), depth(node.right))

        leftDepth = depth(root.left)
        rightDepth = depth(root.right)

        value = leftDepth + rightDepth
        value = max(value, self.diameterOfBinaryTree(root.left))
        value = max(value, self.diameterOfBinaryTree(root.right))

        return value