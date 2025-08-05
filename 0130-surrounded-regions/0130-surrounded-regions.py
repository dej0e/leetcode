from collections import deque


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        num_rows = len(board)
        num_cols = len(board[0])

        def capture(r, c):
            if r < 0 or c < 0 or r == num_rows or c == num_cols or board[r][c] != "O":
                return
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        # 1. DFS - Capture unsurrounded regions (O to T)
        for r in range(num_rows):
            for c in range(num_cols):
                if board[r][c] == "O" and (
                    r in [0, num_rows - 1] or c in [0, num_cols - 1]
                ):
                    capture(r, c)

        # 2. Capture surrounded regions (O to X)
        for r in range(num_rows):
            for c in range(num_cols):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # 3. Uncapture unsurrounded regions (T to O)
        for r in range(num_rows):
            for c in range(num_cols):
                if board[r][c] == "T":
                    board[r][c] = "O"
