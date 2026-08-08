from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        list1 = [[] for _ in range(len(nums) + 1)]

        for item in counter:
            list1[counter[item]].append(item)
        
        ans = []

        for i in range(len(nums), -1, -1):
            if list1[i]:
                for item in list1[i]:
                    ans.append(item)

            if len(ans) == k:
                break

        return ans