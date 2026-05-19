"""
If nums1_left > nums2_right:
    took too many from nums1, move left

If nums2_left > nums1_right:
    took too few from nums1, move right

look by index

we want to make a "correct" left side

the sizes are automatically correct

if 1199 and the other part is 2222, that's bad


"""
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Always binary search the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        A = nums1
        B = nums2

        total = len(A) + len(B)
        half = total // 2

        left = 0
        right = len(A)

        while left <= right:
            i = (left + right) // 2   # how many we take from A
            j = half - i              # how many we take from B

            A_left = A[i - 1] if i > 0 else float("-inf")
            A_right = A[i] if i < len(A) else float("inf")

            B_left = B[j - 1] if j > 0 else float("-inf")
            B_right = B[j] if j < len(B) else float("inf")

            # Correct split
            if A_left <= B_right and B_left <= A_right:
                if total % 2 == 1:
                    return min(A_right, B_right)
                else:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2

            # Took too many from A, move left
            elif A_left > B_right:
                right = i - 1

            # Took too few from A, move right
            else:
                left = i + 1