# max heap

import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            one = heapq.heappop(stones)
            two = heapq.heappop(stones)

            if one < two:
                one, two = two, one
            
            if one != two:
                heapq.heappush(stones, two-one)
            
        return 0 if len(stones) == 0 else -stones[0]
