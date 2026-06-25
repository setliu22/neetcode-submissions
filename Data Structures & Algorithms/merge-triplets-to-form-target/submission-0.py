"""
Values can only increase because merging uses max.

So any triplet that exceeds the target in even one position is unusable.

For every valid triplet, check which target coordinates it provides.

you can merge multiple triplets

CONTINUE if you find a violating triplet

"""

from typing import List

class Solution:
    def mergeTriplets(
        self,
        triplets: List[List[int]],
        target: List[int]
    ) -> bool:
        matched = [False, False, False]

        for triplet in triplets:
            # Cannot use a triplet that exceeds the target
            if any(triplet[i] > target[i] for i in range(3)):
                continue

            # Record the target coordinates this triplet provides
            for i in range(3):
                if triplet[i] == target[i]:
                    matched[i] = True

        return all(matched)