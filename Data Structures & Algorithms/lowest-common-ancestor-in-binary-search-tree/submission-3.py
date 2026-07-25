# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def search(root, p, q):
            if root.val > p.val and root.val > q.val:
                return search(root.left, p, q)
            elif root.val < p.val and root.val < q.val:
                return search(root.right, p, q)
            else:
                return root

        


        return search(root, p, q)




