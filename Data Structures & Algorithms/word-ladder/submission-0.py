"""
For every word, try replacing each character with every letter from a to z.

Most generated words are useless. Only keep a generated word if it exists in the provided wordList.

use BFS for shortest path

technically O(N*L^2*26) but you can always take out constants for big O, theta, Omega

one L for generating a candidate string for each character

"""

from collections import defaultdict, deque
from typing import List

class Solution:
    def ladderLength(
        self,
        beginWord: str,
        endWord: str,
        wordList: List[str]
    ) -> int:
        if endWord not in wordList:
            return 0

        neighbors = defaultdict(list)

        # Include beginWord so it can also generate wildcard patterns.
        words = wordList + [beginWord]

        # Group words that differ by one character.
        #
        # Example:
        # "cat" produces "*at", "c*t", and "ca*"
        # "bat" produces "*at", "b*t", and "ba*"
        #
        # Since both share "*at", they are one transformation apart.
        for word in words:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                neighbors[pattern].append(word)

        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:
            word, length = queue.popleft()

            if word == endWord:
                return length

            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]

                for next_word in neighbors[pattern]:
                    if next_word not in visited:
                        visited.add(next_word)
                        queue.append((next_word, length + 1))

        return 0