"""
Find cycle, return the last edge in the input that belongs to the cycle.

you can't use union find for directed graphs
This is why Course Schedule uses DFS coloring or indegree BFS instead of Union Find.

"if there are multiple answers return the one that appears last in the 
list"
so just return the first one returned by union find which is like simulation
The problem guarantees that the graph started as a tree and exactly one extra edge was added. 
Therefore, there is exactly one cycle.
"""

from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))
        size = [1] * (len(edges) + 1)

        def find(node: int) -> int:
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]

            return node

        def union(a: int, b: int) -> bool:
            root_a = find(a)
            root_b = find(b)

            if root_a == root_b:
                return False

            if size[root_a] < size[root_b]:
                root_a, root_b = root_b, root_a

            parent[root_b] = root_a
            size[root_a] += size[root_b]

            return True

        for a, b in edges:
            if not union(a, b):
                return [a, b]

        return []