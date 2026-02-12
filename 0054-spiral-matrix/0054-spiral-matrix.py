class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        first = 0
        last = len(matrix)-1
        i = 0
        j = len(matrix[0])
        first = 0
        ans = []
        if len(matrix) == 1:
            return matrix[0]

        while first <= last and j > i:

            for k in range(i, j):
                ans.append(matrix[first][k])

            for k in range(first+1, last+1):
                ans.append(matrix[k][j-1])

            if first < last:
                for k in range(j-2, i-1, -1):
                    ans.append(matrix[last][k])

            if i<j-1:
                for k in range(last-1, first, -1):
                    ans.append(matrix[k][i])

            i+=1
            j-=1
            first+=1
            last-=1

        return ans


