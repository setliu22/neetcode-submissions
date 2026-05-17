from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        items = list(count.items())
        items.sort(key=lambda pair: pair[1], reverse=True)

        result = []
        for num, freq in items[:k]:
            result.append(num)

        return result