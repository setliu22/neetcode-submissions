from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            counts = {}

            for char in word:
                if char in counts:
                    counts[char] += 1
                else:
                    counts[char] = 1

            key = tuple(sorted(counts.items()))

            if key not in groups:
                groups[key] = [word]
            else:
                groups[key].append(word)

        return list(groups.values())