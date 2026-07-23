# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, exceed, dont_exceed):
            if node is None:
                return True
            if node.val <= exceed:
                return False
            if node.val >= dont_exceed:
                return False

            return dfs(node.left, exceed, node.val) and dfs(node.right, node.val, dont_exceed)
        
        return dfs(root, float("-inf"), float("inf"))