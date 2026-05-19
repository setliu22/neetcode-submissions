from typing import List

# dont confuse mid with min

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                # mid is on the bigger left side
                # minimum must be to the right of mid
                left = mid + 1
            else:
                # mid is on the smaller right side
                # mid could be the minimum, so keep it
                right = mid

        return nums[left]