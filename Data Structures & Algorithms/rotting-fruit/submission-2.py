class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append([i, j, 0])
        
        self.ans = 0
        
        while queue:
            curr_element = queue.popleft()
            i, j, val = curr_element[0], curr_element[1], curr_element[2]
            print(curr_element)
            if i-1 > -1 and grid[i-1][j] == 1:
                grid[i-1][j] = 2
                queue.append([i-1, j, val + 1])
            if i+1 < len(grid) and grid[i+1][j] == 1:
                grid[i+1][j] = 2
                queue.append([i+1, j, val + 1])
            if j-1 > -1 and grid[i][j-1] == 1:
                grid[i][j-1] = 2
                queue.append([i, j-1, val + 1])
            if j+1 < len(grid[0]) and grid[i][j+1] == 1:
                grid[i][j+1] = 2
                queue.append([i, j+1, val + 1])
            
            self.ans = val

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
            
        return self.ans
