class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # just find the repeat characters
        # find the last x. the characters contained within x cannot be a separate part
        # because y is trapped between the x's it must be included in the substring
        # then once we find another y anything trapped within must be looked at

        n = len(s)

        set1 = set()

        for char in s:
            set1.add(char)

        intervals = []
        
        for char in set1:
            for i in range(0, n):
                if s[i] == char:
                    start = i
                    break

            for i in range(n-1, start-1, -1):
                if s[i] == char:
                    end = i
                    break
            
            intervals.append([start, end])
    
        intervals.sort()

        print(intervals)

        ans = []

        currStart = intervals[0][0] 
        currEnd = intervals[0][1] 

        for i in range(1, len(intervals)):
            if intervals[i][0] < currEnd:
                if intervals[i][1] > currEnd:
                    currEnd = intervals[i][1]
            if intervals[i][0] > currEnd:
                ans.append([currStart, currEnd])
                currStart = intervals[i][0]
                currEnd = intervals[i][1]
        
        ans.append([currStart, currEnd])
        print(ans)

        for i in range(len(ans)):
            ans[i] = ans[i][1]-ans[i][0]+1
        
        return ans

        #noChange = False
        #while not noChange:
        #    intervalCopy = intervals.copy()
        #    for i in range(1, len(intervals)):
        #        if 

            


        

