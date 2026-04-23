class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        def inbound(i, j):
            return (0<=i<len(grid)) and (0<=j<len(grid[0]))
        count = 0
        def calc(i, j):
            if not inbound(i, j):
                return 
            if grid[i][j] == "0":
                return 

            visited.add((i, j))
            for x, y in directions:
                left = x+i
                right = y+j
                if (left, right) not in visited:
                    calc(left, right)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    count+=1
                    calc(i, j)

        return count

            


