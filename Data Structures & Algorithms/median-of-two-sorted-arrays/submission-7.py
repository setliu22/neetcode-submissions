class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # find the amount to take from the first index
        # which determines the amount to take from the second index

        # make sure last element in left side of each is less than first element in right side

        # search smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        bot = 0
        top = len(nums1)

        n = (len(nums1) + len(nums2) + 1) // 2

        
        while bot <= top:
            mid = (bot + top) // 2

            left_of_one = nums1[mid-1] if mid > 0 else float("-inf")
            right_of_one = nums1[mid] if mid < len(nums1) else float("inf")

            other = n - mid

            left_of_two = nums2[other-1] if other > 0 else float("-inf")
            right_of_two = nums2[other] if other < len(nums2) else float("inf")

            if left_of_one > right_of_two: # too many
                top = mid-1
            elif left_of_two > right_of_one: # too little
                bot = mid+1
            else: # you won
                if ((len(nums1) + len(nums2)) % 2) == 0:
                    # take last from left side, first from right side
                    left_side = max(left_of_one, left_of_two)
                    right_side = min(right_of_one, right_of_two)

                    return (left_side + right_side) / 2
                
                else:
                    # left side was made to be bigger, take last element of left side
                    return max(left_of_one, left_of_two)





