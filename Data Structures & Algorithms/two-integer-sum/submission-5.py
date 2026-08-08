class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counter = {}

        for index, item in enumerate(nums):
            if item not in counter:
                counter[item] = [index]
            else:
                counter[item].append(index)
        
        for index, item in enumerate(nums):
            n2 = target - item
            print(f"{item} {n2}")

            if item != n2:
                if (item in counter and n2 in counter):
                    list1 = counter[item] + counter[n2]
                    return sorted(list1)
            else:
                if item in counter and len(counter[item]) > 1:
                    return sorted(counter[item])

