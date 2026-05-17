class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: find where slow and fast meet inside the cycle
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # Phase 2: find the start of the cycle
        # The start of the cycle is the duplicate number
        slow2 = 0

        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow