from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict1 = Counter(s1)

        left = 0

        for index, item in enumerate(s2):
            dict1[item] = dict1.get(item, 0) - 1

            while dict1[item] < 0:
                dict1[s2[left]] += 1
                left += 1
            
            if (max(dict1.values()) == 0):
                return True

        return max(dict1.values()) == 0 # there are only 26 characters

        