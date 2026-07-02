"""
Better local brute force:
Generate its 26 × L possible neighbors
Cost per word: O(26 × L)
store both the word and its distance inside the queue
"""

from collections import deque

class Solution:
    def ladderLength(
        self,
        beginWord: str,
        endWord: str,
        wordList: list[str]
    ) -> int:
        words = set(wordList)

        if endWord not in words:
            return 0

        queue = deque([(beginWord, 1)])

        while queue:
            word, steps = queue.popleft()

            if word == endWord:
                return steps

            for i in range(len(word)):
                for char in "abcdefghijklmnopqrstuvwxyz":
                    if char == word[i]:
                        continue

                    neighbor = word[:i] + char + word[i + 1:]

                    if neighbor in words:
                        words.remove(neighbor)
                        queue.append((neighbor, steps + 1))

        return 0