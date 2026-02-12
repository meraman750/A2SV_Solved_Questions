class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rep = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rep.append([i, j])

        for k in rep:
            i, j = k
            for m in range(len(matrix)):
                matrix[m][j] = 0
            for m in range(len(matrix[0])):
                matrix[i][m] = 0



