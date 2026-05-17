from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # If the tree is empty, there are no levels
        if not root:
            return []

        # Final answer
        res = []

        # Queue starts with the root node
        q = deque([root])

        # Keep going while there are nodes to process
        while q:
            # Stores values for the current level
            level = []

            # Number of nodes currently in this level
            level_size = len(q)

            # Process only the nodes from this level
            for _ in range(level_size):
                # Remove the next node from the front of the queue
                node = q.popleft()

                # Add its value to the current level
                level.append(node.val)

                # Add children to the queue for the next level
                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            # After finishing this level, add it to the result
            res.append(level)

        return res