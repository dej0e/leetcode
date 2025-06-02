from collections import deque


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        num_rows, num_cols = len(image), len(image[0])

        def get_neighbors(coord, actual_color):
            r, c = coord
            res = []
            delta_row = [-1, 0, 1, 0]
            delta_col = [0, 1, 0, -1]
            for i in range(len(delta_row)):
                neighbor_row = r + delta_row[i]
                neighbor_col = c + delta_col[i]
                if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols:
                    if image[neighbor_row][neighbor_col] == actual_color:
                        res.append((neighbor_row, neighbor_col))
            return res

        def bfs(root):
            queue = deque([root])
            visited = [[False for c in range(num_cols)] for r in range(num_rows)]
            r, c = root

            actual_color = image[r][c]
            image[r][c] = color
            visited[r][c] = True
            while len(queue) > 0:
                node = queue.popleft()
                for neighbor in get_neighbors(node, actual_color):
                    r, c = neighbor
                    if visited[r][c]:
                        continue
                    image[r][c] = color
                    queue.append(neighbor)
                    visited[r][c] = True

        bfs((sr, sc))
        return image
