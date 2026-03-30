class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        p_dig = set()
        n_dig = set()
        ans = []
        temp = [["."] * n for i in range(n)]
        
        def is_valid(i, j):
            if j in col or i+j in p_dig or i-j in n_dig:
                return False
            return True   

        def calc(row):
            if row == n:
                t = ["".join(r) for r in temp]
                ans.append(t)
                return 

            for c in range(n):
                if is_valid(row, c):
                    col.add(c)
                    p_dig.add(row+c)
                    n_dig.add(row-c)
                    temp[row][c] = "Q"
                    
                    calc(row+1)
                    
                    col.remove(c)
                    p_dig.remove(row+c)
                    n_dig.remove(row-c)
                    temp[row][c] = "."

        calc(0)
        return ans


