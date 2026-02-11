from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        ROWS, COLS = len(grid), len(grid[0])

        count = 0

        def bfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0":
                return
            q = deque([(r, c)])
            grid[r][c] = 0
            delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            while q:
                r, c = q.popleft()
                for dr, dc in delta:
                    nr = r+dr
                    nc = c+dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] =="1":
                        q.append((nr,nc))
                        grid[nr][nc] = '0'

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r, c)
                    count += 1
        return count
