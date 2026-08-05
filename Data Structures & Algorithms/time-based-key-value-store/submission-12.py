# max heap

import heapq

class TimeMap:

    def __init__(self):
        self.storage = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.storage:
            self.storage[key] = [(timestamp, value)]
        else:
            self.storage[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.storage:
            return ""

        values = self.storage[key]

        print(values)

        if values[0][0] > timestamp:
            return ""

        bot = 0
        top = len(values)-1

        while bot < top:
            upper_mid = (bot + top + 1) // 2
            if values[upper_mid][0] <= timestamp:
                # could be the last one
                bot = upper_mid
            else:
                top = upper_mid-1

        return values[bot][1]
