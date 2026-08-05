# max heap

import heapq

class TimeMap:

    def __init__(self):
        self.storage = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.storage:
            self.storage[key] = [(-timestamp, value)]
        
        else:
            heapq.heappush(self.storage[key], (-timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.storage:
            copy = self.storage[key][:]
            while copy:
                if -copy[0][0] <= timestamp:
                    print(-copy[0][0])
                    return copy[0][1]
                heapq.heappop(copy)

        return ""