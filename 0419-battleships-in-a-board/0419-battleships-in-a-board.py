class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ROWS = len(board)
        COLS = len(board[0])
        # directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        # def dfs(r, c):
        #     if min(r, c) < 0 or r >= ROWS or c >= COLS or board[r][c] != "X":
        #         return

        #     board[r][c] = "."
        #     for dr, dc in directions:
        #         nr = r + dr
        #         nc = c + dc
        #         dfs(nr, nc)

        # count = 0
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if board[r][c] == "X":
        #             dfs(r, c)
        #             count += 1
        # return count

        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "X":
                    if (r == 0 or board[r-1][c] == ".") and (c == 0 or board[r][c-1] == "."):
                        count += 1
        return count