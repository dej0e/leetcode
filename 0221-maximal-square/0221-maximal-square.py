class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        num_rows = len(matrix)
        num_cols = len(matrix[0])
        best = 0
        dp: List[List[int]] = [[0 for _ in range(num_cols)] for _ in range(num_rows)]
        for r in range(num_rows):
            if matrix[r][0] == "0":
                continue  # skip 0 cells
            dp[r][0] = int(matrix[r][0])
            best = max(dp[r][0], best)

        for c in range(num_cols):
            if matrix[0][c] == "0":
                continue  # skip 0 cells
            dp[0][c] = int(matrix[0][c])
            best = max(dp[0][c], best)

        for r in range(1, num_rows):
            for c in range(1, num_cols):
                if matrix[r][c] == "0":
                    continue  # skip 0 cells
                dp[r][c] = 1 + min(dp[r - 1][c], dp[r - 1][c - 1], dp[r][c - 1])
                best = max(dp[r][c], best)

        return best * best
