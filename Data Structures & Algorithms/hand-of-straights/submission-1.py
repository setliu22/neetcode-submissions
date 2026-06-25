from typing import List
from collections import Counter
import heapq

"""
A min heap to find the smallest remaining value.
A frequency map to remove specific consecutive values efficiently.

The heap always gives us the smallest remaining card, and every card is removed exactly once.

There are three failure checks:

if len(hand) % groupSize != 0:
    return False

This fails immediately when the cards cannot be divided into equal-sized groups.

The main failure condition is:

if count[value] == 0:
    return False

This checks whether a required consecutive card is missing. For example, if the group needs [3, 4, 5] but there is no 4, it returns False.

The last check is:

if value != min_heap[0]:
    return False

This ensures the heap stays synchronized with the frequency map. A value can only be removed from the heap when it is currently the smallest remaining value.

We ran out of a larger required card while a smaller card still remains. Therefore, a future group cannot be completed.
1123
when we try to put 2 we can just see that 1 is still there therefore abort
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