class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        root = [i for i in range(n)]
        size = [1] * n

        ans = n

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
                return False
            
            if size[root_a] < size[root_b]:
                root_a, root_b = root_b, root_a

            # root_a always the larger one
            
            root[root_b] = root_a
            size[root_a] += size[root_b] 
            return True

        for a, b in edges:
            if union(a, b):
                ans -= 1

        return ans

