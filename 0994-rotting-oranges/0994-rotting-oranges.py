from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        time = 0
        delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        while fresh > 0 and len(q) > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in delta:
                    nr = r + dr
                    nc = c + dc
                    if (
                        0 <= nr < ROWS
                        and 0 <= nc < COLS
                        and grid[nr][nc] == 1
                    ):
                        q.append((nr, nc))
                        grid[nr][nc] = 2
                        fresh-=1
            time+=1
        return -1 if fresh > 0 else time 
