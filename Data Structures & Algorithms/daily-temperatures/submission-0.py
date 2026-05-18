# The stack does not store the temperatures directly. It stores their indexes.
# you can easily access the values using the indices
# subtract indices to get distance metrics

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # stores indexes of days waiting for a warmer temperature

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                old_day = stack.pop()
                res[old_day] = i - old_day

            stack.append(i)

        return res