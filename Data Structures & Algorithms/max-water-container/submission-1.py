class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # start two pointers, one at the beginning and one at the end

        p1 = 0
        p2 = len(heights) - 1

        ans = 0

        # you need to ALWAYS MOVE, the heights[p1] < saved_p1 is just a stopping condition

        while p1 < p2:

            if heights[p1] <= heights[p2]:
                ans = max(ans, (p2 - p1) * heights[p1])
                saved_p1 = heights[p1]
                while p1 < p2:
                    p1 += 1
                    if heights[p1] > saved_p1:
                        break
            else:
                ans = max(ans, (p2 - p1) * heights[p2])
                saved_p2 = heights[p2]
                while p1 < p2:
                    p2 -= 1
                    if heights[p2] > saved_p2:
                        break
        
        return ans