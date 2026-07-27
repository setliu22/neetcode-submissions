import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = [(grid[0][0], 0, 0)]
        visited = {(0, 0)}

        while heap:
            curr_height, i, j = heapq.heappop(heap)

            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                return curr_height

            if i - 1 >= 0 and (i - 1, j) not in visited:
                visited.add((i - 1, j))
                heapq.heappush(
                    heap,
                    (max(curr_height, grid[i - 1][j]), i - 1, j)
                )

            if j - 1 >= 0 and (i, j - 1) not in visited:
                visited.add((i, j - 1))
                heapq.heappush(
                    heap,
                    (max(curr_height, grid[i][j - 1]), i, j - 1)
                )

            if i + 1 < len(grid) and (i + 1, j) not in visited:
                visited.add((i + 1, j))
                heapq.heappush(
                    heap,
                    (max(curr_height, grid[i + 1][j]), i + 1, j)
                )

            if j + 1 < len(grid[0]) and (i, j + 1) not in visited:
                visited.add((i, j + 1))
                heapq.heappush(
                    heap,
                    (max(curr_height, grid[i][j + 1]), i, j + 1)
                )