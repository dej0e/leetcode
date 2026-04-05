class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)
        
        sizes = defaultdict(int)
        label = 2
        
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        def out_of_bounds(r, c):
            return min(r, c) < 0 or r >= N or c >= N
        
        def dfs_area(r, c, label):
            if out_of_bounds(r, c) or grid[r][c] != 1:
                return 0

            size_island = 1
            grid[r][c] = label
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                size_island += dfs_area(nr, nc, label)
            return size_island
        
        # 1. Precompute area and assign the areas to unique labels in sizes area map
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    sizes[label] = dfs_area(r, c, label)
                    label += 1
        
        def connect(r, c):
            area = 1
            visited = set() #track visited labels of islands
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if not out_of_bounds(nr, nc) and grid[nr][nc] in sizes and grid[nr][nc] not in visited:
                    area += sizes[grid[nr][nc]]
                    visited.add(grid[nr][nc])
            return area

        area = max(sizes.values()) if sizes else 0
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 0:
                    area = max(area, connect(r, c))

        return area