class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [["."]*n for _ in range(n)]
        cols=set()
        posdia=set()
        negdia= set()
        def backtrack(row):
            if row == n:
                result.append(["".join(r) for r in board])
                return
            for col in range(n):
                if col in cols:
                    continue
                if row + col in posdia:
                    continue
                if row - col in negdia:
                    continue
                board[row][col] = "Q"
                cols.add(col)
                posdia.add(row + col)
                negdia.add(row - col)
                backtrack(row + 1)
                board[row][col] = "."
                cols.remove(col)
                posdia.remove(row + col)
                negdia.remove(row - col)
        backtrack(0)
        return result