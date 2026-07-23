# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        currSol = False

        def small_tester(node, subNode):
            if node is None and subNode is not None:
                return False
            elif node is not None and subNode is None:
                return False
            elif node is None and subNode is None:
                return True
            else:
                return (node.val == subNode.val) and small_tester(node.left, subNode.left) and small_tester(node.right, subNode.right)

        queue = deque([root])

        while queue:
            curr = queue.popleft()
            if curr.val == subRoot.val:
                currSol = small_tester(curr, subRoot)
                if currSol:
                    break
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

        return currSol