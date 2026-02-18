class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        
        r, c = rStart, cStart
        ans = [[r, c]]
        
        steps = 1
        
        while len(ans) < rows * cols:
            for _ in range(steps):
                c += 1
                if 0 <= r < rows and 0 <= c < cols:
                    ans.append([r, c])
            
            for _ in range(steps):
                r += 1
                if 0 <= r < rows and 0 <= c < cols:
                    ans.append([r, c])
            
            steps += 1
            
            for _ in range(steps):
                c -= 1
                if 0 <= r < rows and 0 <= c < cols:
                    ans.append([r, c])
            
            for _ in range(steps):
                r -= 1
                if 0 <= r < rows and 0 <= c < cols:
                    ans.append([r, c])
            
            steps += 1
        
        return ans
