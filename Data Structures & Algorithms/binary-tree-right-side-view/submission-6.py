# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# last node in a row

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        queue = deque([root])

        ans = []

        tempqueue = deque()
        
        while queue:

            while queue:
                curr = queue.popleft()
                tempqueue.append(curr)
            
            ans.append(curr.val)
            
            while tempqueue:
                curr = tempqueue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

        return ans
        

        