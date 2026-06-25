from typing import List
from collections import Counter
import heapq

"""
A min heap to find the smallest remaining value.
A frequency map to remove specific consecutive values efficiently.

The heap always gives us the smallest remaining card, and every card is removed exactly once.
"""

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        min_heap = list(count.keys())
        heapq.heapify(min_heap)

        while min_heap:
            start = min_heap[0]

            for value in range(start, start + groupSize):
                if count[value] == 0:
                    return False

                count[value] -= 1

                if count[value] == 0:
                    if value != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)

        return True