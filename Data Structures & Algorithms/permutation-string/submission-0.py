# we have already considered earlier windows, and once the new character arrives, any useful new window must include that new right-side character. If including it breaks the counts, we shrink from the left until the current window becomes possible again.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = {}

        for char in s1:
            need[char] = need.get(char, 0) + 1

        left = 0

        for right in range(len(s2)):
            char = s2[right]
            need[char] = need.get(char, 0) - 1

            while need[char] < 0:
                left_char = s2[left]
                need[left_char] = need.get(left_char, 0) + 1
                left += 1

            if right - left + 1 == len(s1):
                return True

        return False