import heapq
import math

# CLOSEST POINTS to origin

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            heapq.heappush(heap, (-math.sqrt(point[0]*point[0] + point[1]*point[1]), tuple(point)))
            if len(heap) > k:
                heapq.heappop(heap)
        
        ans = []

        for element in heap:
            ans.append([element[1][0], element[1][1]])
        
        return ans
