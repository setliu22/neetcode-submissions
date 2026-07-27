import copy

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        arraycopyP = [([0]*len(heights[0])) for _ in range(len(heights))]
        arraycopyA = [([0]*len(heights[0])) for _ in range(len(heights))]

        def labeler(i, j, origin):
            if origin == "P" and arraycopyP[i][j] == 0:
                arraycopyP[i][j] = 1
                print(f"{i}{j}")
            elif origin == "A" and arraycopyA[i][j] == 0:
                arraycopyA[i][j] = 1
            if i-1 > -1 and heights[i-1][j] >= heights[i][j]:
                if origin == "P" and arraycopyP[i-1][j] == 0:
                    labeler(i-1, j, origin)
                elif origin == "A" and arraycopyA[i-1][j] == 0:
                    labeler(i-1, j, origin)
            if i+1 < len(heights) and heights[i+1][j] >= heights[i][j]:
                if origin == "P" and arraycopyP[i+1][j] == 0:
                    labeler(i+1, j, origin)
                elif origin == "A" and arraycopyA[i+1][j] == 0:
                    labeler(i+1, j, origin)
            if j-1 > -1 and heights[i][j-1] >= heights[i][j]:
                if origin == "P" and arraycopyP[i][j-1] == 0:
                    labeler(i, j-1, origin)
                elif origin == "A" and arraycopyA[i][j-1] == 0:
                    labeler(i, j-1, origin)
            if j+1 < len(heights[0]) and heights[i][j+1] >= heights[i][j]:
                if origin == "P" and arraycopyP[i][j+1] == 0:
                    labeler(i, j+1, origin)
                elif origin == "A" and arraycopyA[i][j+1] == 0:
                    labeler(i, j+1, origin)          

        # leftmost column
        for i in range(len(heights)):
            labeler(i, 0, "A")

        # top row no double counting cuz +1
        for j in range(1, len(heights[0])):
            labeler(0, j, "A")

        # rightmost column
        for i in range(len(heights)):
            labeler(i, len(heights[0])-1, "P")

        # bottom row no double counting +1
        for j in range(len(heights[0])):
            labeler(len(heights)-1, j, "P")
        
        self.ans = []

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if arraycopyA[i][j] > 0 and arraycopyP[i][j] > 0:
                    self.ans.append([i, j])

        return self.ans