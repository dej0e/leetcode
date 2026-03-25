from collections import deque


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacVisit = [[False] * COLS for _ in range(ROWS)]
        atlVisit = [[False] * COLS for _ in range(ROWS)]

        pac = []
        atl = []
        for r in range(ROWS):
            atl.append((r, COLS-1))
            pac.append((r, 0))

        for c in range(COLS):
            atl.append((ROWS-1, c))
            pac.append((0, c))

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        def bfs(source, ocean):
            q = deque(source)
            while q:
                r, c = q.popleft()
                ocean[r][c] = True
                for dr, dc in directions:
                    nr = dr + r
                    nc = dc + c
                    if min(nr, nc) < 0 or nr >= ROWS or nc >= COLS:
                        continue
                    if ocean[nr][nc] == True or heights[nr][nc] < heights[r][c]:
                        continue
                    q.append((nr, nc))
                    ocean[nr][nc] = True

        bfs(atl, atlVisit)
        bfs(pac, pacVisit)
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if pacVisit[r][c] and atlVisit[r][c]:
                    res.append((r, c))
        return res