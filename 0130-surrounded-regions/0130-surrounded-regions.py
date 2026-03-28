from collections import deque


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS = len(board)
        COLS = len(board[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()

        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if (r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1) and board[r][c] == "O":
                    q.append((r, c))
        while q:
            r, c = q.popleft()
            visited.add((r, c))
            board[r][c] = "T"
            for dr, dc in directions:
                nr = dr + r
                nc = dc + c
                if (
                    min(nr, nc) < 0
                    or nr >= ROWS
                    or nc >= COLS
                    or (nr, nc) in visited
                    or board[nr][nc] != "O"
                ):
                    continue
                q.append((nr, nc))

    

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
