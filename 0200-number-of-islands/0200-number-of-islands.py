from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        def bfs(row, col):
            q = deque()
            q.append((row, col))
            while q:
                r, c = q.popleft()
                
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if min(nr, nc) < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == "0":
                        continue
                    grid[nr][nc] = "0"
                    q.append((nr, nc))
        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1
        return islands