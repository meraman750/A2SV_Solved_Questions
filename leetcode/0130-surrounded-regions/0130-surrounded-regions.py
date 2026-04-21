class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        visited = set()

        def inboud(i, j):
            return (0 <= i < len(board)) and (0 <= j < len(board[0]))

        def calc(i, j):
            if not inboud(i, j):
                return True

            if board[i][j] == "X":
                return False
            
            res.append((i, j))
            surround = False
            visited.add((i, j))
            for l, r in directions:
                x = i + l
                y = j + r
                if (x, y) not in visited:
                    if calc(x, y):
                        surround = True
            return surround

        for i in range(len(board)):
            for j in range(len(board[0])):
                res = []
                if (i, j) not in visited and  board[i][j] == "O" and not calc(i, j):
                    for x, y in res:
                        board[x][y] = "X"


                    
            
        