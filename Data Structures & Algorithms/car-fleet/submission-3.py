class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr1 = sorted(zip(position, speed), reverse = True)

        stack = []

        for pos, speed in arr1:

            # only add if you arrive slower than a car closer to the end

            time = (target - pos) / speed

            if not stack or time > stack[-1]:
                stack.append(time)

        print(stack)

        return len(stack)
            