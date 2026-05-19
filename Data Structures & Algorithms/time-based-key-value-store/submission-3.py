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

        # OPTION 2:
        # We find the first timestamp that is greater than the query timestamp.
        # Then the answer is one index before that.
        left = 0
        right = len(values)

        while left < right:
            mid = (left + right) // 2

            if values[mid][0] <= timestamp:
                # values[mid] is valid.
                # But maybe there is a later valid timestamp.
                # Move left past mid.
                left = mid + 1
            else:
                # values[mid] is too big.
                # Keep mid, because it might be the first too-big timestamp.
                # We do NOT do mid - 1 here because right is excluded.
                right = mid

        # left is now the first timestamp greater than the query.
        # So left - 1 is the last timestamp less than or equal to the query.
        index = left - 1

        if index >= 0:
            return values[index][1]

        return ""


"""
OTHER OPTION:

OPTION 1:
Use right as the final answer index.

left = 0
right = len(values) - 1

while left <= right:
    mid = (left + right) // 2

    if values[mid][0] <= timestamp:
        # values[mid] is valid.
        # Search farther right for a later valid timestamp.
        left = mid + 1
    else:
        # values[mid] is too big.
        # Remove mid from the search.
        # We use mid - 1 because right is included in this version.
        right = mid - 1

# After the loop:
# right is the last timestamp <= query timestamp.
# left is the first timestamp > query timestamp.
answer_index = right

if answer_index >= 0:
    return values[answer_index][1]

return ""

MAIN DIFFERENCE:

Option 1:
    right = len(values) - 1
    while left <= right
    right = mid - 1
    answer_index = right

Option 2:
    right = len(values)
    while left < right
    right = mid
    answer_index = left - 1

Why the difference?

In Option 1, right is included, so if mid is too big, you remove mid by doing:

    right = mid - 1

In Option 2, right is excluded, so if mid is too big, you keep mid as the boundary by doing:

    right = mid
"""