class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        inc = []
        ans = 0

        for i in range(len(heights)):
            start = i
            while inc and inc[-1][1] > heights[i]:
                idx, val = inc.pop()
                ans = max(ans, val * (i-idx))
                start = idx
            inc.append([start, heights[i]])
        
        print(inc)
        print(ans)
        for i in inc:
            ans = max(ans, i[1] * (len(heights) - i[0]))
        
        return ans