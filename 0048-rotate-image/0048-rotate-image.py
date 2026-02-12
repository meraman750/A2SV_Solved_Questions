class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ans = [[] for _ in range(len(matrix[0]))]
        
        for i in range(len(matrix[0])):
            for j in range(len(matrix)-1, -1, -1):
                ans[i].append(matrix[j][i])

        matrix[:] = ans
