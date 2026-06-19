"""
maxEndingHere[i] = largest product of a subarray ending exactly at i
minEndingHere[i] = smallest product of a subarray ending exactly at i

you have three choices

nums[i]                         # start a new subarray
maxEndingHere[i - 1] * nums[i] # extend previous maximum
minEndingHere[i - 1] * nums[i] # extend previous minimum

maxEndingHere[i] = max(
    nums[i],
    maxEndingHere[i - 1] * nums[i],
    minEndingHere[i - 1] * nums[i]
)

minEndingHere[i] = min(
    nums[i],
    maxEndingHere[i - 1] * nums[i],
    minEndingHere[i - 1] * nums[i]
)
"""

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        current_max = nums[0]
        current_min = nums[0]
        answer = nums[0]

        for x in nums[1:]:
            previous_max = current_max
            previous_min = current_min

            current_max = max(
                x,
                previous_max * x,
                previous_min * x
            )

            current_min = min(
                x,
                previous_max * x,
                previous_min * x
            )

            answer = max(answer, current_max)

        return answer