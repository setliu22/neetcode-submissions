class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        dict1 = {}
        currAns = 0
        n = len(s)
        index = 0
        left = 0

        while index < n:
            char = s[index]
            if char not in dict1 or dict1[char] < left:
                dict1[char] = index
                currAns += 1
                ans = max(ans, currAns)
            else:
                old_index = dict1[char]
                currAns -= (old_index-left) + 1
                currAns += 1
                left = old_index + 1
                dict1[char] = index
            index += 1

        return ans