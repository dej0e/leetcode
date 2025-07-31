from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])

        def get_neighbor(node):
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

        def bfs(root):
            queue = deque([root])
            r, c = root

            grid[r][c] = "0"
            while len(queue) > 0:
                node = queue.popleft()
                for neighbor in get_neighbor(node):
                    r, c = neighbor
                    if grid[r][c] == "0":
                        continue
                    grid[r][c] = "0"
                    queue.append(neighbor)

        count = 0
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == "0":
                    continue
                bfs((r, c))
                count += 1
        return count
