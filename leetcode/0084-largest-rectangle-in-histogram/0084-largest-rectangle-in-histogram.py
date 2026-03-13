class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        bound = {}
        for i in range(len(heights)):
            bound[i] = [-1, len(heights)]
        inc = []
        for i in range(len(heights)):
            while inc and heights[inc[-1]] > heights[i]:
                bound[inc[-1]][1] = i 
                inc.pop()
            inc.append(i)
        
        inc = []
        for i in range(len(heights)-1, -1, -1):
            while inc and heights[inc[-1]] > heights[i]:
                bound[inc[-1]][0] = i
                inc.pop()
            inc.append(i)
        
        ans = 0
        for key, val in bound.items():
            ans = max(ans, heights[key] * (val[1] - val[0] -1))
        return ans



