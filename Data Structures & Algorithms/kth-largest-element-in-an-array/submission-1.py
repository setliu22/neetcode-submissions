import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # treat it like a stream, use kth largest method

        heap = []

        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        
        return heap[0]
