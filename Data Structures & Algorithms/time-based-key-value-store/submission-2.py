class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []

        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        values = self.store[key]

        left = 0
        right = len(values) - 1

        while left <= right:
            mid = (left + right) // 2

# So the +1 and -1 are not random. They force the pointers to cross, and after they cross, right is the answer index.

            if values[mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid - 1

        if right >= 0:
            return values[right][1]

        return ""