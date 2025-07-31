from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])

        def get_neighbors(node):
            r, c = node
            neighbors = []
            delta_row = [-1, 0, 1, 0]
            delta_col = [0, 1, 0, -1]
            for i in range(len(delta_row)):
                nei_r = r + delta_row[i]
                nei_c = c + delta_col[i]
                if 0 <= nei_r < num_rows and 0 <= nei_c < num_cols:
                    neighbors.append((nei_r, nei_c))
            return neighbors

        queue = deque()
        fresh = 0
        minutes = 0

        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
                elif grid[r][c] == 1:
                    fresh += 1

        while len(queue) > 0:
            node = queue.popleft()
            r, c, minute = node
            for neighbor in get_neighbors((r, c)):
                nr, nc = neighbor
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc, minute + 1))
                    minutes = minute + 1

        return minutes if fresh == 0 else -1
