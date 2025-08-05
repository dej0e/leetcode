from collections import deque


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        num_rows = len(heights)
        num_cols = len(heights[0])
        pac = [[False] * num_cols for _ in range(num_rows)]
        atl = [[False] * num_cols for _ in range(num_rows)]

        def get_neighbors(r, c, ocean):
            delta_row = [-1, 0, 1, 0]
            delta_col = [0, 1, 0, -1]
            for i in range(len(delta_row)):
                nr = r + delta_row[i]
                nc = c + delta_col[i]
                if (
                    0 <= nr < num_rows
                    and 0 <= nc < num_cols
                    and heights[r][c] <= heights[nr][nc]
                    and ocean[nr][nc] == False
                ):
                    yield nr, nc

        def bfs(source, ocean):
            queue = deque(source)
            while queue:
                r, c = queue.popleft()
                ocean[r][c] = True
                for nr, nc in get_neighbors(r, c, ocean):
                    queue.append((nr, nc))

        pacific = []
        atlantic = []

        for c in range(num_cols):
            pacific.append((0, c))
            atlantic.append((num_rows - 1, c))

        for r in range(num_rows):
            pacific.append((r, 0))
            atlantic.append((r, num_cols - 1))

        bfs(pacific, pac)
        bfs(atlantic, atl)

        res = []
        for r in range(num_rows):
            for c in range(num_cols):
                if atl[r][c] and pac[r][c]:
                    res.append((r, c))
        return res
