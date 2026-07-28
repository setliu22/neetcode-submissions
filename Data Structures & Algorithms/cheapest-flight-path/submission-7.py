import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # heap stores (distance, node, # flights used)
        heap = [(0, src, 0)]

        graph = {i: [] for i in range(n)}

        for source, destination, cost in flights:
            graph[source].append((destination, cost))

        visited = set()

        while heap:
            dist, node, flights = heapq.heappop(heap)

            if flights > k+1:
                continue
            
            # add to visited only when popped from the heap
            visited.add((node, flights))

            if node == dst:
                return dist

            for item in graph[node]:
                if item not in visited:
                    heapq.heappush(heap, (dist+item[1], item[0], flights+1))

        return -1  
            