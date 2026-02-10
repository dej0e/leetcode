class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        queue = deque()

        if grid[0][0] == 1 or grid[ROWS - 1][COLS - 1] == 1:
            return -1

        deltas = [
            (-1, 0),
            (-1, 1),
            (0, 1),
            (1, 1),
            (1, 0),
            (1, -1),
            (0, -1),
            (-1, -1),
        ]
        queue.append((0, 0, 1))
        visited.add((0, 0))
        while len(queue) > 0:
            for _ in range(len(queue)):
                r, c, length = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length

                for dr, dc in deltas:
                    nr = r + dr
                    nc = c + dc
                    if (
                        nr < 0
                        or nc < 0
                        or nr >= ROWS
                        or nc >= COLS
                        or (nr, nc) in visited
                        or grid[nr][nc] == 1
                    ):
                        continue
                    queue.append((nr, nc, length + 1))
                    visited.add((nr, nc))
        return -1
