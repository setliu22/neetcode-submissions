# get indegrees, a and b can be placed now because nothing has to come before them
# Since b -> c, -= 1
# After collecting all rules, topological sort turns those rules into a valid alphabet order.

from typing import List
from collections import defaultdict, deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Every unique character must appear in the result
        adj = defaultdict(set)
        indegree = {}

        for word in words:
            for char in word:
                indegree[char] = 0

        # Build ordering rules from adjacent words
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            min_len = min(len(w1), len(w2))

            # Invalid case:
            # "abc" before "ab" is impossible because "ab" is a prefix
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""

            # Find the first different character
            for j in range(min_len):
                c1 = w1[j]
                c2 = w2[j]

                if c1 != c2:
                    # Since w1 comes before w2, c1 must come before c2
                    if c2 not in adj[c1]:
                        adj[c1].add(c2)
                        indegree[c2] += 1
                    break

        # Topological sort
        queue = deque()

        for char in indegree:
            if indegree[char] == 0:
                queue.append(char)

        result = []

        while queue:
            char = queue.popleft()
            result.append(char)

            for nei in adj[char]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    queue.append(nei)

        # If we could not use every character, there was a cycle
        if len(result) != len(indegree):
            return ""

        return "".join(result)