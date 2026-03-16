class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        
        i = target
        count = 0
        while i > 1:
            if maxDoubles > 0 and i%2 == 0:
                i//=2
                maxDoubles-=1
            else:
                i-=1
            if maxDoubles == 0:
                return count + i
            count+=1
        return count