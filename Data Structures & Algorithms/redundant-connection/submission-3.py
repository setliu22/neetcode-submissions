class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        root = [i for i in range(len(edges))]
        size = [1] * len(edges)

        def find(node):
            while node != root[node]:
                root[node] = root[root[node]]
                node = root[node]
            return node

        def union(a, b):
            root_a = find(a)
            root_b = find(b)

            print(f"{a} and {b} and {root_a} and {root_b}")

            if root_a == root_b:
                return True
            
            if size[root_a] < size[root_b]:
                root_a, root_b = root_b, root_a

            # root_a always the larger one
            
            root[root_b] = root_a
            size[root_a] += size[root_b]

            return False 

        for a, b in edges:
            if union(a-1, b-1):
                return [a, b]