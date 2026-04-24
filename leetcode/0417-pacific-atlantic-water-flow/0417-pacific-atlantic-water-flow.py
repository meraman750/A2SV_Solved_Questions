class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        n, m = len(heights), len(heights[0])

        def inbound(i, j):
            return (0 <= i <len(heights)) and (0 <= j < len(heights[0]))

        def calc(n, i, j, visited):
            # print(n, i, j)
            if inbound(i, j) and heights[i][j] > n:
                return set()
            if not inbound(i, j):
                if j < 0 or i < 0:
                    return {1}
                return {2}
            visited.add((i, j))
            

            temp = set()
            for l, r in directions:
                if (i+l, r+j) not in visited:
                    # print("uyad")
                    temp |= calc(heights[i][j], i+l, r+j, visited)
                    # visited.add((i+l, r+j))
            # print(i, j, temp)
            return temp
        # print(calc(inf, 1, 1, set()))

        ans = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                visited = set()
                if len(calc(float("inf"), i, j, visited)) == 2:
                    ans.append([i, j])
        return ans
