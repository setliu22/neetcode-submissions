class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        pacific = [[False] * cols for _ in range(rows)]
        atlantic = [[False] * cols for _ in range(rows)]

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(i, j, visited):

            visited[i][j] = True

            for di, dj in directions:
                ni, nj = i + di, j + dj

                if (
                    0 <= ni < rows
                    and 0 <= nj < cols
                    and not visited[ni][nj]
                    and heights[ni][nj] >= heights[i][j]
                ):
                    dfs(ni, nj, visited)

        # Pacific: top + left
        for i in range(rows):
            dfs(i, 0, pacific)

        for j in range(cols):
            dfs(0, j, pacific)

        # Atlantic: bottom + right
        for i in range(rows):
            dfs(i, cols - 1, atlantic)

        for j in range(cols):
            dfs(rows - 1, j, atlantic)

        ans = []

        for i in range(rows):
            for j in range(cols):
                if pacific[i][j] and atlantic[i][j]:
                    ans.append([i, j])

        return ans