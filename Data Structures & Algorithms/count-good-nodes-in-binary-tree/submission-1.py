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

        def smallHelper(node, prev):
            if node.val >= prev:
                self.ans += 1
                prev = node.val
            if node.left:
                smallHelper(node.left, prev)
            if node.right:
                smallHelper(node.right, prev)

        smallHelper(root, float("-inf"))

        return self.ans
        