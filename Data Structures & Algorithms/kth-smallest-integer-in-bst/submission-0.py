class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.answer = None

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            self.count += 1
            if self.count == k:
                self.answer = node.val
                return

            inorder(node.right)

        inorder(root)
        return self.answer