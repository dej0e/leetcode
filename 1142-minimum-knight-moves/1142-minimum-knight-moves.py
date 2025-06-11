from collections import deque


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        def get_neighbors(coord):
            res = []
            row, col = coord
            delta_row = [-2, -1, 1, 2, 2, 1, -1, -2]
            delta_col = [1, 2, 2, 1, -1, -2, -2, -1]
            for i in range(len(delta_row)):
                r = row + delta_row[i]
                c = col + delta_col[i]
                res.append((r, c))
            return res

        def bfs(root):
            visited = set()
            queue = deque([root])
            steps = 0
            while len(queue) > 0:
                n = len(queue)
                for _ in range(n):
                    node = queue.popleft()
                    if node == (x, y):
                        return steps
                    for neighbor in get_neighbors(node):
                        r, c = neighbor
                        if neighbor in visited:
                            continue
                        queue.append(neighbor)
                        visited.add(neighbor)
                steps += 1
            return steps

        return bfs((0, 0))
