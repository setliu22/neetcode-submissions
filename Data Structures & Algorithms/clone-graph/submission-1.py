"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
            
        dict1 = {node: Node(node.val)}

        queue = deque([node])

        while queue:
            curr_node = queue.popleft()
            print(curr_node.val)
            neighbors = curr_node.neighbors

            for i in range(len(neighbors)):
                print(f"{neighbors[i].val}!")

            for item in neighbors:
                if item not in dict1:
                    dict1[item] = Node(item.val)
                    queue.append(item)
                
                dict1[curr_node].neighbors.append(dict1[item])
        
        return dict1[node]

