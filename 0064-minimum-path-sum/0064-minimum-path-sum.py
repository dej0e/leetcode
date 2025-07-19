class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for r in range(m):
            dp[r][0] = dp[r - 1][0] + grid[r][0] if r else grid[r][0]

        for c in range(n):
            dp[0][c] = dp[0][c - 1] + grid[0][c] if c else grid[0][c]

        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = min(dp[r - 1][c], dp[r][c - 1]) + grid[r][c]

        return dp[m - 1][n - 1]
