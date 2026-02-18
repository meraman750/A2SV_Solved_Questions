class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d = {}
        for i in range(len(names)):
            d[heights[i]] = names[i]
        for i in range(len(names)):
            for j in range(len(names)-i-1):
                if heights[j] < heights[j+1]:
                    heights[j], heights[j+1] = heights[j+1], heights[j]
        return [d[i] for i in heights]
        
        # x = zip(names, heights)
        # for i in x:
        #     print(i)

        # # for i in range(len(names)):
        # #     for j in range(len(names)-i):
        # #         # if x[j][1] > x[j+1][1]:
        # #         #     x[j], x[j+1] = x[j+1], x[j]
        # return [i[1] for i in x]

