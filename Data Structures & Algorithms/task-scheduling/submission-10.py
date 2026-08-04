import heapq
import queue

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        heap = []

        # if thing at top of heap has time that you are at, do it
        # pop it and add back with the time it can be used

        # do most frequent tasks first

        tasks = Counter(tasks)

        for key, value in tasks.items():
            heapq.heappush(heap, (-value, 0))

        time = 0

        queue = deque()

        while heap or queue:
            print(heap)
            if queue:
                while queue and queue[0][1] == time:
                    element = queue.popleft()
                    print(element)
                    heapq.heappush(heap, element)

            if heap:
                if heap[0][1] <= time:
                    freq, not_used_time = heapq.heappop(heap)
                    freq += 1
                    if freq < 0:
                        queue.append((freq, time+n+1))

            time += 1
        
        return time