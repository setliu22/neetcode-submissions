# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        ans = []
        queue = deque([root])

        while queue:
            # get nodes in current level out of queue
            level_ans = []
            level_nodes = deque()
            while queue:
                curr = queue.popleft()
                level_ans.append(curr.val)
                level_nodes.append(curr)

            ans.append(level_ans)

            # then take all children of current level and add to queue
            while level_nodes:
                curr = level_nodes.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        
        return ans