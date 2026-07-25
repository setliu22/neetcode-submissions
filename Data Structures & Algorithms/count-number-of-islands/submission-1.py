class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        self.ans = 0

        def labeler(i, j, d):
            grid[i][j] = "X"
            if i-1 > -1 and grid[i-1][j] == "1":
                print(str(i-1)+" "+str(j)+"...."+str(d))
                labeler(i-1, j, d+1)
            if i+1 < len(grid) and grid[i+1][j] == "1":
                labeler(i+1, j, d+1)
            if j-1 > -1 and grid[i][j-1] == "1": 
                labeler(i, j-1, d+1)
            if j+1 < len(grid[0]) and grid[i][j+1] == "1":
                labeler(i, j+1, d+1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.ans += 1
                    labeler(i, j, 0)
        
        return self.ans