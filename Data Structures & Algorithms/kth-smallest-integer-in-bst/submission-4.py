class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0

        def inorder(node):
            if not node:
                return None

            left = inorder(node.left)
            if left is not None:
                return left

            self.count += 1
            if self.count == k:
                return node.val

            right = inorder(node.right)
            if right is not None:
                return right

        return inorder(root)