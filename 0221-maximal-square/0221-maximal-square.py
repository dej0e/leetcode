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

# For convenience, we'll say a square ends in a cell if its bottom-right corner is located in that cell.

# If the cell at (r, c) is 0 then there's no 1-filled square that ends in this cell. Otherwise, we have to figure out how to compute dp[r][c] from previous subproblems.

# Let's consider a cell (r,c) where matrix[r][c] = 1 and dp[r][c] = k for some positive integer k.

# For a square of size k to exist at the cell (r,c), then these conditions must be also true:

#     A square of size k - 1 that ends at (r - 1, c).
#     A square of size k - 1 that ends at (r, c - 1).
#     A square of size k - 1 that ends at (r - 1, c - 1).

# For a square to have size k - 1 at the cells (r - 1, c), (r, c - 1), and (r - 1, c - 1), the values dp[r - 1][c], dp[r][c - 1], and dp[r - 1][c - 1] all have to be greater or equal than k - 1.

# From this observation, we can obtain the following transition:

# dp[r][c] = 1 + min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1])

# This state essentially means look at the minimum sized square that ends at one of the following cells: (r - 1, c), (r, c - 1), (r - 1, c - 1) Take that value and after adding 1, we can obtain dp[r][c].

# Time Complexity: O(r*c)
