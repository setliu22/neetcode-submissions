# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        
        queue = deque([root])

        while queue:
            curr_root = queue.popleft()

            curr_root.left, curr_root.right = curr_root.right, curr_root.left

            if curr_root.left:
                queue.append(curr_root.left)
            
            if curr_root.right:
                queue.append(curr_root.right)
        
        return root