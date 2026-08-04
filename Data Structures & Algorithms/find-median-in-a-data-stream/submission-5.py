"""
use a min heap and a max heap of even size

if greater than max, send it to the min heap

the heaps should separate data into two halves no matter the order of addition

send first element to one heap

1,2,3 (max heap) 8.9.9,9 (min heap)

1, 2, 3, 4, 5, 6

2 4 5 6 3 1

3, 2, 1 / 4, 5, 6

the number of elements probably the most helpful part
the median just from max if size max heap larger, min if size min haep larger, average if equal size

move from one heap to the other if greater than 2 difference

100000000000000, 1, 0 / 1000, 1000
"""

import heapq

class MedianFinder:

    def __init__(self):
        self.small_size_max = []
        self.large_size_min = []

    def addNum(self, num: int) -> None:
        # if greater than the min of the right side, add to the right side
        # if less than max of left side, add to left side
        if self.small_size_max == [] and self.large_size_min == []:
            self.small_size_max.append(-num)
            return
        elif self.large_size_min == []:
            self.large_size_min.append(num)
            if -self.small_size_max[0] > self.large_size_min[0]:
                self.small_size_max[0], self.large_size_min[0] = -self.large_size_min[0], -self.small_size_max[0]
            return
        
        if num < -self.small_size_max[0]:
            heapq.heappush(self.small_size_max, -num)
        else:
            heapq.heappush(self.large_size_min, num)

        # rebalance if greater than 2 absolute value difference to easily get the median
        if abs(len(self.small_size_max) - len(self.large_size_min)) > 1:
            if len(self.small_size_max) > len(self.large_size_min):
                val = heapq.heappop(self.small_size_max)
                heapq.heappush(self.large_size_min, -val)
            else:
                val = heapq.heappop(self.large_size_min)
                heapq.heappush(self.small_size_max, -val)

    def findMedian(self) -> float:
        if len(self.small_size_max) > len(self.large_size_min):
            #print(f"{self.small_size_max} {self.large_size_min} {-self.small_size_max[0]}")
            return -self.small_size_max[0]
        elif len(self.small_size_max) < len(self.large_size_min):
            #print(f"{self.small_size_max} {self.large_size_min} {self.large_size_min[0]}")
            return self.large_size_min[0]
        else:
            #print(f"{self.small_size_max} {self.large_size_min} {(-self.small_size_max[0]+self.large_size_min[0])/2}")
            return (-self.small_size_max[0]+self.large_size_min[0])/2

        
        