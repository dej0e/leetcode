from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        ROWS, COLS = len(grid), len(grid[0])

        count = 0
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        def bfs(row, col):
            q = deque()
            grid[row][col] = 0
            q.append((row, col))
            while q:
                r, c = q.popleft()
                
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if min(nr, nc) < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] != "1":
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = "0"
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r, c)
                    count += 1
        return count
                
                
            