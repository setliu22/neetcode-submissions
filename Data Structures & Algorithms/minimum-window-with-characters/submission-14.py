from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # probably just max of values again
        # while loop can just be as long as adding 1 to that doesn't make it > 0
        # so once you go negative see if you can move the left pointer up!

        dict1 = Counter(t)

        ans = float("inf")
        storedInterval = [0, -1]

        left = 0

        for index, item in enumerate(s):
            #print(dict1)
            if item in dict1:
                dict1[item] -= 1

            if max(dict1.values()) <= 0: # if the max value <= 0, then do the while loop
                while (left < index and s[left] not in dict1) or (left < index and dict1[s[left]] < 0):
                    if s[left] in dict1:
                        dict1[s[left]] += 1
                    left += 1

            if max(dict1.values()) == 0:
                if index - left + 1 < ans:
                    ans = index - left + 1
                    storedInterval = [left, index]
                    #print(storedInterval)

        return s[storedInterval[0]:storedInterval[1] + 1]
