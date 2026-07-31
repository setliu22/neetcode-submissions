import heapq
from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # for heap you just need unique elements, Counter keeps track of element counts

        counter = Counter(hand)
        heap = list(counter.keys())
        heapq.heapify(heap)

        while heap:

            curr_value = heap[0]

            for i in range(groupSize): # 0 1 for group size 2
                print(curr_value+i)
                if counter[curr_value+i] == 0:
                    return False
                counter[curr_value+i] -= 1
            
            while heap and counter[heap[0]] == 0:
                heapq.heappop(heap)
            
        return True