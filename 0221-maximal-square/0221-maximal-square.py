class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # # Bottom Up DP
        # if not matrix:
        #     return 0
        # ROWS = len(matrix)
        # COLS = len(matrix[0])
        # dp = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        # maxLen = 0
        # for r in range(ROWS-1, -1, -1):
        #     for c in range(COLS - 1, -1, -1):
        #         if matrix[r][c] == "1":
        #             dp[r][c] = 1 + min(dp[r][c+1], dp[r+1][c+1], dp[r+1][c])
        #             maxLen = max(maxLen, dp[r][c])
        # return maxLen**2

        # # Top Down DP
        ROWS = len(matrix)
        COLS = len(matrix[0])
        cache = {}

        def dfs(r, c):
            if r >= ROWS or c >= COLS:
                return 0
            if (r, c) in cache:
                return cache[(r,c)]
            cache[(r, c)] = 0
            down = dfs(r + 1, c)
            diag = dfs(r + 1, c + 1)
            right = dfs(r, c + 1)
            if matrix[r][c] == "1":
                cache[(r, c)] = 1 + min(down, diag, right)
            return cache[(r, c)]
        dfs(0, 0)
        return max(cache.values())**2
