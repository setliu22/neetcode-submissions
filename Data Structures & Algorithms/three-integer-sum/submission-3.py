class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        n = len(nums)

        p1 = 0

        ans = []

        for p1 in range(n-2):
            if p1 > 0 and nums[p1] == nums[p1-1]:
                continue
            p2 = p1 + 1
            p3 = n - 1

            while p2 < p3:

                if nums[p1] + nums[p2] + nums[p3] == 0:
                    # after this change p2 AND p3 to a new number
                    ans.append([nums[p1], nums[p2], nums[p3]])

                    saved_p2 = nums[p2]
                    saved_p3 = nums[p3]
                    while p2 < p3 and nums[p2] == saved_p2:
                        p2 += 1
                    while p2 < p3 and nums[p3] == saved_p3:
                        p3 -= 1
                    
                elif nums[p1] + nums[p2] + nums[p3] < 0:
                    saved_p2 = nums[p2]
                    while p2 < p3 and nums[p2] == saved_p2:
                        p2 += 1

                else:
                    saved_p3 = nums[p3]
                    while p2 < p3 and nums[p3] == saved_p3:
                        p3 -= 1



                
        return ans