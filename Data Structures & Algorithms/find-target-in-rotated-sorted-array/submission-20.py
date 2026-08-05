class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        if n == 1:
            return 0 if nums[0] == target else -1

        bot = 0
        top = len(nums)-1

        counter = 0

        while bot <= top and counter < 50:
            counter += 1
            middle = (bot+top) // 2
            print(f"{bot} {middle} {top}")
            if nums[bot] <= nums[middle]:
                if nums[bot] <= target <= nums[middle]:
                    top = middle
                    break
                else:
                    bot = middle+1
            else:
                if nums[middle] <= target <= nums[top]:
                    bot = middle
                    break
                else:
                    top = middle-1

        # if you didn't find anything just return -1
        if bot > top:
            return -1

        # lowkey just do the binary search separately
        while bot <= top:
            middle = (bot+top) // 2
            print(middle)
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                top = middle-1
            else:
                bot = middle+1

        return -1
