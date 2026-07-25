class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.ans = 0

        self.curr_val = 0

        def labeler(i, j):
            grid[i][j] = "X"
            self.curr_val += 1
            if i-1 > -1 and grid[i-1][j] == 1:
                labeler(i-1, j)
            if i+1 < len(grid) and grid[i+1][j] == 1:
                labeler(i+1, j)
            if j-1 > -1 and grid[i][j-1] == 1: 
                labeler(i, j-1)
            if j+1 < len(grid[0]) and grid[i][j+1] == 1:
                labeler(i, j+1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    labeler(i, j)
                    self.ans = max(self.ans, self.curr_val)
                    self.curr_val = 0
        
        return self.ans