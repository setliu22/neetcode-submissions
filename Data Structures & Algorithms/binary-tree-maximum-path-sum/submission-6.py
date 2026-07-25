# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.ans = root.val

        def dfs(node):
            if node is None:
                return 0
            leftSide = dfs(node.left)
            rightSide = dfs(node.right)
    
            self.ans = max(self.ans, leftSide+rightSide+node.val)

            greaterSide = max(leftSide+node.val, rightSide+node.val)
            return max(greaterSide, 0)

        dfs(root)

        return self.ans