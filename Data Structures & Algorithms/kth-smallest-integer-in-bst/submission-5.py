# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # in order traversal

        self.count = k

        def dfs(node):
            if node is None:
                return None
            if node.left is not None:
                val = dfs(node.left)
                if val is not None:
                    return val
            self.count -= 1
            if self.count == 0:
                return node.val
            if node.right is not None:
                val = dfs(node.right)
                if val is not None:
                    return val

        return dfs(root)