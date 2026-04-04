class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()
        direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if min(r, c) < 0 or r >= ROWS or c >= COLS or (r, c) in visited or board[r][c] != word[i]:
                return False

            visited.add((r,c))
            found = (dfs(r-1, c, i + 1) or 
                    dfs(r, c + 1, i + 1) or 
                    dfs(r + 1, c, i + 1) or 
                    dfs(r, c - 1, i + 1))
            visited.remove((r,c))
            return found


        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False