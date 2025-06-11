from collections import deque

INF = 2147483647

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # WRITE YOUR BRILLIANT CODE HERE

        num_rows = len(rooms)
        num_cols = len(rooms[0])

        def get_neighbors(coord):
            r, c = coord
            res = []
            delta_row = [0, 1, 0, -1]
            delta_col = [1, 0, -1, 0]
            for i in range(len(delta_row)):
                row = r + delta_row[i]
                col = c + delta_col[i]
                if row >= 0 and row < num_rows and col >= 0 and col < num_cols:
                    res.append((row, col))
            return res

        queue = deque()
        for r in range(num_rows):
            for c in range(num_cols):
                if rooms[r][c] == 0:
                    queue.append((r, c))

        while len(queue) > 0:
            r, c = queue.popleft()
            for neighbor_r, neighbor_c in get_neighbors((r, c)):
                if rooms[neighbor_r][neighbor_c] == INF:
                    rooms[neighbor_r][neighbor_c] = rooms[r][c] + 1
                    queue.append((neighbor_r, neighbor_c))
