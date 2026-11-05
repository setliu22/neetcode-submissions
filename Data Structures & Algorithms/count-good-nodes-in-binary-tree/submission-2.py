# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # if not good, overwrite that value with the larger value above

        if root is None:
            return 0

        self.ans = 0

        def dfs(node, prev):
            if node.val >= prev:
                self.ans += 1
                prev = node.val
            if node.left:
                dfs(node.left, prev)
            if node.right:
                dfs(node.right, prev)

        dfs(root, float("-inf"))

        return self.ans
        