from typing import Optional


# Definition for a Node.
# class Node:
#     def __init__(self, val=0, neighbors=None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if node is None:
            return None

        # Maps each original node to its cloned node.
        clones = {}

        def dfs(current: "Node") -> "Node":
            # If this node was already cloned, reuse the clone.
            # This prevents infinite loops in graphs with cycles.
            if current in clones:
                return clones[current]

            copy = Node(current.val)
            clones[current] = copy

            for neighbor in current.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)