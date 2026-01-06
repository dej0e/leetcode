class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        colSet = set()
        posDiag = set() # r+c 
        negDiag = set() # r-c

        res = []
        board = [["."] * n for _ in range(n)]
        def backtrack(row):
            if row == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for col in range(n):
                if col in colSet or (row+col) in posDiag or (row-col) in negDiag:
                    continue
                colSet.add(col)
                posDiag.add(row+col)
                negDiag.add(row-col)
                board[row][col] = "Q"
                backtrack(row+1)
                colSet.remove(col)
                posDiag.remove(row+col)
                negDiag.remove(row-col)
                board[row][col] = "."
        
        backtrack(0)
        return res