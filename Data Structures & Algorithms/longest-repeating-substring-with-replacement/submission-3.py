class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # bruh answered the wrong question
        # you can choose any character and replace them
        # once you run out of characters to replace you have to move the window
        # you want as many of the most common character as you can get

        ans = 0

        dict1 = {}

        left = 0 # left pointer for length of interval/number of elements

        for index, char in enumerate(s):
            dict1[char] = dict1.get(char, 0) + 1

            while ((index - left + 1) - max(dict1.values())) > k:
                dict1[s[left]] -= 1
                left += 1

            ans = max(ans, index - left + 1)
        
        return ans