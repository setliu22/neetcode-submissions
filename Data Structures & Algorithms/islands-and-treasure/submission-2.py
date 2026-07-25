from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # start bfs outwards from treasure chests

        queue = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append([i, j, 0])
        
        while queue:
            curr_element = queue.popleft()
            i, j, val = curr_element[0], curr_element[1], curr_element[2]
            print(curr_element)
            if i-1 > -1 and grid[i-1][j] == 2147483647:
                grid[i-1][j] = val + 1
                queue.append([i-1, j, val + 1])
            if i+1 < len(grid) and grid[i+1][j] == 2147483647:
                grid[i+1][j] = val + 1
                queue.append([i+1, j, val + 1])
            if j-1 > -1 and grid[i][j-1] == 2147483647:
                grid[i][j-1] = val + 1
                queue.append([i, j-1, val + 1])
            if j+1 < len(grid[0]) and grid[i][j+1] == 2147483647:
                grid[i][j+1] = val + 1
                queue.append([i, j+1, val + 1])