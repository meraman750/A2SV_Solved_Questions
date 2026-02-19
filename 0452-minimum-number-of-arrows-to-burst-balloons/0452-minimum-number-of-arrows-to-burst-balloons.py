class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        # minn = points[0][0]
        # maxx = points[0][1]
        ans = 1
        cur = points[0][1]
        for i in points[1:]:
            if i[0] > cur:
                ans+=1
                cur = i[1]
            # if points[i][0] <= maxx:
            #     minn = max(minn, points[i][0])
            #     maxx = min(maxx, points[i][1])
            # else:
            #     ans += 1
            #     minn = points[i][0]
            #     maxx = points[i][1]
        return ans
