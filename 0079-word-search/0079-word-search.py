class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS = len(board)
        COLS = len(board[0])
        visited = [[False] * COLS for _ in range(ROWS)]

        def dfs(r, c, i):
            if i == len(word):
                return True

            if (r < 0 or c < 0 or r >= ROWS or c >= COLS):
                return False
            
            if visited[r][c] or board[r][c] != word[i]:
                return False
            
            
            visited[r][c] = True
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            
            res = False
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if dfs(nr, nc, i + 1):
                    return True
            visited[r][c] = False
            return False
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False
