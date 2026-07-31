class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # dp ish with furthest you can reach from that index?
        # you can also CHOOSE to jump shorter than max jump length

        if len(nums) == 1:
            return True

        currFurthest = nums[0]

        if currFurthest == 0:
            return False

        for i in range(1, len(nums)):
            if i > currFurthest:
                return False
            if i == len(nums)-1:
                return True
            if i == currFurthest:
                currFurthest = nums[i]+i
            currFurthest = max(currFurthest, nums[i]+i)
            print(currFurthest)
