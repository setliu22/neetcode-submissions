# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return None
        self.currMax = 0

        # pass up the max of left/right to upper node
        # update max with left+right-1

        def dfs(root):
            if root is None:
                return 0
            leftSide = 1+dfs(root.left)
            rightSide = 1+dfs(root.right)
            self.currMax = max(self.currMax, leftSide+rightSide-1)
            return max(leftSide, rightSide)

        dfs(root)

        return self.currMax-1


