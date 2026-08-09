class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        # maybe always eliminate the longest interval for a speciifc start

        intervals.sort()

        i = 0

        ans = 0

        currInterval = intervals[0]
        minRightFromPrev = currInterval[1]
        leftFromPrev = currInterval[0]

        n = len(intervals)

        for i in range(1, n):
            interval = intervals[i]

            if interval[0] < minRightFromPrev: # if it's strictly within the min right, we still need to delete but keep the min right
                minRightFromPrev = min(minRightFromPrev, interval[1]) 
                ans += 1

            # else it's just past then interval and no deletion necessary but update vals
            else:
                minRightFromPrev = interval[1]

        
        return ans
