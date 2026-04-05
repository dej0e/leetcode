from collections import deque


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        pacVisit = set()
        atlVisit = set()
        pacific = []
        atlantic = []
        for r in range(ROWS):
            pacific.append((r, 0))
            atlantic.append((r, COLS - 1))
        
        for c in range(COLS):
            pacific.append((0, c))
            atlantic.append((ROWS - 1, c))
        
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        def bfs(row, col, ocean):
            q = deque()
            q.append((row, col))
            ocean.add((row, col))
            while q:
                r, c = q.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc 
                    if min(nr, nc) < 0 or nr >= ROWS or nc >= COLS or heights[nr][nc] < heights[r][c] or (nr, nc) in ocean:
                        continue
                    q.append((nr, nc))
                    ocean.add((nr, nc))
        
        for r, c in pacific:
            bfs(r, c, pacVisit)
        for r, c in atlantic:
            bfs(r, c, atlVisit)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacVisit and (r,c) in atlVisit:
                    res.append([r, c])

        return res