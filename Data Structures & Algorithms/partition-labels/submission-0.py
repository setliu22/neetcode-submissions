"""
First, record the last index where every character appears.

While scanning a partition, keep track of the farthest last occurrence of every character seen so far.

end = max(end, last[s[i]])

Once the current index reaches end, the partition can safely end because every character inside it has no occurrence later in the string.

Then, start the next partition
"""

from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}

        for i, char in enumerate(s):
            last[char] = i

        result = []
        start = 0
        end = 0

        for i, char in enumerate(s):
            end = max(end, last[char])

            if i == end:
                result.append(end - start + 1)
                start = i + 1

        return result