class CountSquares:

    def __init__(self):
        self.grid = [[0] * 1001 for _ in range(1001)]

    def add(self, point: List[int]) -> None:
        self.grid[point[0]][point[1]] += 1

    def count(self, point: List[int]) -> int:

        x = point[0]
        y = point[1]
        
        finalAns = 0
        ans = 1

        # try to find points to left, then find line above/below
        for i in range(x - 1, -1, -1):
            if self.grid[i][y] > 0:
                ans *= self.grid[i][y]

                side = x - i

                # find line above
                j = y - side
                if j >= 0:
                    if self.grid[i][j] > 0 and self.grid[x][j] > 0:
                        finalAns += ans * self.grid[i][j] * self.grid[x][j]

                # find line below
                j = y + side
                if j <= 1000:
                    if self.grid[i][j] > 0 and self.grid[x][j] > 0:
                        finalAns += ans * self.grid[i][j] * self.grid[x][j]
            
            ans = 1

        # try to find points to right, then find line above/below
        for i in range(x + 1, 1001):
            if self.grid[i][y] > 0:
                ans *= self.grid[i][y]

                side = i - x

                # find line above
                j = y - side
                if j >= 0:
                    if self.grid[i][j] > 0 and self.grid[x][j] > 0:
                        finalAns += ans * self.grid[i][j] * self.grid[x][j]

                # find line below
                j = y + side
                if j <= 1000:
                    if self.grid[i][j] > 0 and self.grid[x][j] > 0:
                        finalAns += ans * self.grid[i][j] * self.grid[x][j]
            
            ans = 1
        
        return finalAns