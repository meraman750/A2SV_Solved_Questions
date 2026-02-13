class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = []

        row = 0
        up = True
        for col in range(len(mat[0])):
            temp = []
            i = 0
            j = col
            while i < len(mat) and j >= 0:
                temp.append(mat[i][j])
                i+=1 
                j-=1
            if up:
                ans.extend(reversed(temp))
                up = False
            else:
                ans.extend(temp)
                up = True
        
        for row in range(1, len(mat)):
            temp = []
            i = row
            j = len(mat[0])-1
            while i < len(mat) and j >= 0:
                temp.append(mat[i][j])
                i+=1 
                j-=1
            if up:
                ans.extend(reversed(temp))
                up = False
            else:
                ans.extend(temp)
                up = True
        return ans

            

