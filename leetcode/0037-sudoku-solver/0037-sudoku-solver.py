class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = defaultdict(set)
        cols = defaultdict(set)
        sqr = defaultdict(set)

        for i in range(9):
            for j in range(9):
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                sqr[(i//3, j//3)].add(board[i][j])

        def back(i, j):
            if i >= 9:
                return True
            if j >= 9:
                return back(i+1, 0)

            if board[i][j] != ".":
                return back(i, j+1)

            for k in range(1, 10):
                x = str(k)
                if x not in rows[i] and x not in cols[j] and x not in sqr[(i//3, j//3)]:
                    board[i][j] = str(k)
                    rows[i].add(x)
                    cols[j].add(x)
                    sqr[(i//3, j//3)].add(x)

                    if back(i, j+1):
                        return True

                    board[i][j] = "."
                    rows[i].remove(x)
                    cols[j].remove(x)
                    sqr[(i//3, j//3)].remove(x)
            return False
        back(0, 0)


                


        