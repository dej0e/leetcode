class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        ROWS = len(grid)
        COLS = len(grid[0])
        maxarea = 0
        def bfs(row, col):
            q = deque()
            q.append((row, col))
            grid[row][col] = 0
            area = 0
            while q:
                r, c = q.popleft()
                area += 1
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if min(nr, nc) < 0 or nr >= ROWS or nc >= COLS:
                        continue
                    if grid[nr][nc] == 0:
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = 0
            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = bfs(r, c)
                    maxarea = max(maxarea, area)    
        return maxarea