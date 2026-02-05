class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for i in range(left, right+1):
            c = False
            for j in ranges:
                if j[0] <= i <= j[-1]:
                    c = True 
                    break
            if c == False:
                return False
        return True 
