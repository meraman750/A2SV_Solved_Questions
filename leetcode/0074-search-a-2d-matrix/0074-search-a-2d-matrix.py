class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i in matrix:
            x = set(i)
            if target in x:
                return True
        return False