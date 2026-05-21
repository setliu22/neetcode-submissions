class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-num for num in nums]
        heapq.heapify(heap)

        result = None

        for _ in range(k):
            result = -heapq.heappop(heap)

        return result