class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        i = 0

        ans = []
        currInterval = intervals[0]

        n = len(intervals)

        for i in range(1, n):
            interval = intervals[i]

            if interval[0] <= currInterval[1]:
                currInterval[1] = max(currInterval[1], interval[1])

            else:
                ans.append(currInterval)
                currInterval = interval

        ans.append(currInterval)
        
        return ans
