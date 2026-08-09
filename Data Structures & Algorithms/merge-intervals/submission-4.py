class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        i = 0

        ans = []
        currInterval = intervals[0]

        n = len(intervals)

        if n == 1:
            ans.append(currInterval)
            return ans

        for i in range(1, n):
            interval = intervals[i]

            if interval[0] <= currInterval[1]:
                currInterval[1] = max(currInterval[1], interval[1])
                if i == n - 1:
                    ans.append(currInterval)
            else:
                ans.append(currInterval)
                currInterval = interval
                if i == n - 1:
                    ans.append(currInterval)
        
        return ans
