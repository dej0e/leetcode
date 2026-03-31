class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        ROWS = len(matrix)
        COLS = len(matrix[0])
        dp = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        maxLen = 0
        for r in range(ROWS-1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                if matrix[r][c] == "1":
                    dp[r][c] = 1 + min(dp[r][c+1], dp[r+1][c+1], dp[r+1][c])
                    maxLen = max(maxLen, dp[r][c])
        return maxLen**2
