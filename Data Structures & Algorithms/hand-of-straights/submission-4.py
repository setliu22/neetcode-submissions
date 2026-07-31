import heapq
from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        counter = Counter(hand)

        heap = hand.copy()
        heapq.heapify(heap)

        while heap:
            curr_value = heap[0]

            for i in range(groupSize):
                if counter[curr_value + i] == 0:
                    return False

                counter[curr_value + i] -= 1

            while heap and counter[heap[0]] == 0:
                heapq.heappop(heap)

        return True