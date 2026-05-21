from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        counts = Counter(tasks)

        # max heap using negative counts
        heap = [-count for count in counts.values()]
        heapq.heapify(heap)

        # stores tasks cooling down as: (time_when_available, remaining_count)
        cooldown = deque()

        time = 0

        while heap or cooldown:
            time += 1

            # any tasks whose cooldown expired become available again
            while cooldown and cooldown[0][0] <= time:
                _, count = cooldown.popleft()
                heapq.heappush(heap, count)

            if heap:
                count = heapq.heappop(heap)
                count += 1  # because count is negative, this means one task was used

                if count < 0:
                    cooldown.append((time + n + 1, count))

        return time