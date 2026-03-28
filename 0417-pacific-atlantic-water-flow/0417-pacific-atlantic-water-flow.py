from collections import deque


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        pacVisit = [[False] * COLS for _ in range(ROWS)]
        atlVisit = [[False] * COLS for _ in range(ROWS)]
        pac = []
        atl = []
        for r in range(ROWS):
            pac.append((r, 0))
            atl.append((r, COLS - 1))

        for c in range(COLS):
            pac.append((0, c))
            atl.append((ROWS - 1, c))

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def bfs(source, ocean):
            q = deque(source)
            while q:
                r, c = q.popleft()
                ocean[r][c] = True

                for dr, dc in directions:
                    nr = dr + r
                    nc = dc + c
                    if 0 <= nr < ROWS and 0 <= nc < COLS and ocean[nr][nc] != True and heights[nr][nc] >= heights[r][c]:
                        q.append((nr, nc))

        res = []
        bfs(pac, pacVisit)
        bfs(atl, atlVisit)

        for r in range(ROWS):
            for c in range(COLS):
                if pacVisit[r][c] == True and atlVisit[r][c] == True:
                    res.append((r, c))
        return res
