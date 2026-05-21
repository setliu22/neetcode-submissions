"""
heap      = available tasks by remaining count
queue     = tasks cooling down until a future time
time      = current CPU cycle

there is also a compact mathematical solution approach
"""

from collections import Counter

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        counts = Counter(tasks).values()

        max_freq = max(counts)
        num_max = sum(1 for count in counts if count == max_freq)

        return max(
            len(tasks),
            (max_freq - 1) * (n + 1) + num_max
        )