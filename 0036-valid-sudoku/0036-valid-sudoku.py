class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def isValid(row, col):
            num = board[row][col]
            if num == ".":
                return True

            # Check for col if same num si present
            for i in range(ROWS):
                if i != row and num == board[i][col]:
                    return False

            # check for row if same num is present
            for i in range(COLS):
                if i != col and num == board[row][i]:
                    return False

            # check corresponding 3x3 if same num is present
            row3, col3 = (row // 3) * 3, (col // 3) * 3
            for i in range(row3, row3 + 3):
                for j in range(col3, col3 + 3):
                    if (i != row or j != col) and num == board[i][j]:
                        return False
            return True
            
        for i in range(ROWS):
            for j in range(COLS):
                if not isValid(i, j):
                    return False
        return True
