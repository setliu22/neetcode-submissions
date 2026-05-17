class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node):
            nonlocal ans

            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            path = left + right
            if path > ans:
                ans = path

            return left + 1 if left > right else right + 1

        dfs(root)
        return ans