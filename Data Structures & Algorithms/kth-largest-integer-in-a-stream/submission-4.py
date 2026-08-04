import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # the heap keeps the top k largest, the smaller of the two is the node of interest
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)

        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)

        if len(self.nums) > self.k:
            heapq.heappop(self.nums)

        return self.nums[0]

        
