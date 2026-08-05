# find side that's sorted

# first place where you go from large to small

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if left side is sorted, look at right half
        # if right side is sorted, look at left half
        # if length is 2 and left is greater than right return left index+1

        bot = 0
        top = len(nums)-1

        timer = 0

        while bot < top and timer < 30:
            timer += 1
            middle = (bot+top) // 2
            print(f"{bot} {top} {middle}")
            if nums[bot:middle+1][0] > nums[bot:middle+1][-1]:
                if (middle-bot) == 1:
                    return nums[bot:middle+1][-1]
                top = middle
            elif nums[middle:top+1][0] > nums[middle:top+1][-1]:
                if (top-middle) == 1:
                    return nums[middle:top+1][-1]
                bot = middle
            else:
                return nums[0]

        # if you didn't find anything just return len(nums)
        return nums[0]