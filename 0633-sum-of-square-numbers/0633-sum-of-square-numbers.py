class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = floor(sqrt(c))
        while left <= right:
            cur = (left ** 2) + (right ** 2)
            if cur > c:
                right-=1
            elif cur < c:
                left+=1
            else:
                return True
        return False
