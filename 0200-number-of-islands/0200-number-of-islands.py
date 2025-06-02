from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_cols, num_rows = len(grid[0]), len(grid)
        visited = [[False for c in range(num_cols)] for r in range(num_rows)]

        def get_neighbors(coord):
            res = []
            row, col = coord
            delta_row = [-1, 0, 1, 0]
            delta_col = [0, 1, 0, -1]
            for i in range(len(delta_row)):
                neighbor_c = col + delta_col[i]
                neighbor_r = row + delta_row[i]
                if 0 <= neighbor_r < num_rows and 0 <= neighbor_c < num_cols:
                    res.append((neighbor_r, neighbor_c))
            return res

        def bfs(start):
            queue = deque([start])
            r, c = start
            visited[r][c] = True
            while len(queue) > 0:
                node = queue.popleft()
                for neighbor in get_neighbors(node):
                    r, c = neighbor
                    if grid[r][c] == '0' or visited[r][c]:
                        continue
                    queue.append(neighbor)
                    visited[r][c] = True

        count = 0
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == '0' or visited[r][c]:
                    continue
                bfs((r, c))
                count += 1
        return count
