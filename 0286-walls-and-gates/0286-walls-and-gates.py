from collections import deque

INF = 2147483647


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        ROWS, COLS = len(rooms), len(rooms[0])
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append((r, c))
        level = 1
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr+r, dc+c
                    if min(nr, nc) < 0 or nr >= ROWS or nc >= COLS or rooms[nr][nc] != INF:
                        continue
                    q.append((nr, nc))
                    rooms[nr][nc] = level
            level += 1
        
