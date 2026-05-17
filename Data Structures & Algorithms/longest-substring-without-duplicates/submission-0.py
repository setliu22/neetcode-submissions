class Solution:
# repeat character not always far left
# key trick: when you run into duplicate character, only way to get longer than what you've already seen is to include this new one, exclude the old one, and see how far you can get
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        longest = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            longest = max(longest, right - left + 1)

        return longest