class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        ans = 0

        set1 = set(nums)

        for item in set1:
            if item - 1 not in set1:
                longest = 0
                while item in set1:
                    longest += 1
                    item += 1
                ans = max(ans, longest)

        return ans