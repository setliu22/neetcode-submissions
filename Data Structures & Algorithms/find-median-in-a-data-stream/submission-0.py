import heapq

class MedianFinder:

    def __init__(self):
        self.small = []  # max heap, stored as negative values
        self.large = []  # min heap

    def addNum(self, num: int) -> None:
        # Add to max heap first
        heapq.heappush(self.small, -num)

        # Move largest from small to large to preserve ordering
        heapq.heappush(self.large, -heapq.heappop(self.small))

        # Keep small at least as large as large
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]

        return (-self.small[0] + self.large[0]) / 2