class Solution:
    def trap(self, height: List[int]) -> int:
        # start at left side
        # if you reach a higher wall than before, go until you hit a higher wall
        # add the contributions of each index


        n = len(height)

        p1 = 0

        ans = 0
        currAns = 0

        # the 'wall' at the right side has height 0
        # you should only add stuff after hitting a wall at least as high as current

        # if an attempted left wall reaches the end without succeeding, try the next index as a wall
        currHeight = height[0]
        largestSoFar = 0
        largestSoFarIndex = 0

        while p1 < n - 1:
            p2 = p1 + 1

            largestSoFar = height[p2]
            largestSoFarIndex = p2

            while p2 < n and height[p2] < currHeight:
                currAns += currHeight - height[p2]
                if height[p2] > largestSoFar:
                    largestSoFar = height[p2]
                    largestSoFarIndex = p2
                
                p2 += 1

            # reached a taller or same height, safely add and reset everything
            if p2 < n and height[p2] >= currHeight:
                ans += currAns
                currAns = 0
                largestSoFar = 0
                p1 = p2
                currHeight = height[p2]
            # reached the end and you need to use largestSoFar
            # pass through recalculating
            elif p2 == n:
                currAns = 0
                for i in range(p1 + 1, largestSoFarIndex):
                    currAns += largestSoFar - height[i]

                ans += currAns
                currAns = 0
                currHeight = largestSoFar
                p1 = largestSoFarIndex

        return ans



