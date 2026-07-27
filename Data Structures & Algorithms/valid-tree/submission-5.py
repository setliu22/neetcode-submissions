from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        self.ans = True

        if len(edges) != n-1:
            return False

        edgeArray = [[] for _ in range(n)]

        for a, b in edges:
            edgeArray[a].append(b)
            edgeArray[b].append(a)
        
        visited = [0] * n

        queue = deque([0])

        while queue:
            currNode = queue.popleft()
            if not visited[currNode]:
                visited[currNode] = 1
            
            for new in edgeArray[currNode]:
                if not visited[new]:
                    queue.append(new)

        return sum(visited) == n