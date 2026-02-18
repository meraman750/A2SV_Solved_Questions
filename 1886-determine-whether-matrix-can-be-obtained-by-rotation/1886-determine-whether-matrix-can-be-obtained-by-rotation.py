class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        def rotat(arr):
            temp = []
            for j in range(len(arr)):
                cur = []
                for i in range(len(arr)-1, -1, -1):
                    cur.append(arr[i][j])
                temp.append(cur)
            return temp
        
        for i in range(4):
            if mat == target:
                return True
            mat = rotat(mat)
        return False
            