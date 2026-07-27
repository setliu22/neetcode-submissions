import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def dist(a, b):
            return abs(a[0]-b[0]) + abs(a[1]-b[1])

        heap = [(0, 0)]

        visited = set()

        cost = 0

        a = points[0]

        while len(visited) != len(points):
            current_dist, current_point = heapq.heappop(heap)

            var = current_point in visited
            print(f"{current_point} is {var}")

            if current_point not in visited:
                visited.add(current_point)

                cost += current_dist

                for i in range(len(points)):
                    if i not in visited:
                        heapq.heappush(heap, (dist(points[current_point], points[i]), i))
        
        return cost
            

            
            
        

        