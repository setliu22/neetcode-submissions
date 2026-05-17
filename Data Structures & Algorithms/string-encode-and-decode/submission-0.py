from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for word in strs:
            encoded += str(len(word)) + "#" + word

        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            # Find the delimiter after the length
            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            # The actual word starts after "#"
            start = j + 1
            word = s[start:start + length]

            result.append(word)

            # Move to the next encoded word
            i = start + length

        return result