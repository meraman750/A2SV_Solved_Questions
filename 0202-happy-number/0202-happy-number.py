class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        
        naod = set()
        
        while n not in naod:
            naod.add(n)
            ans = 0
            k = str(n)
            for i in k:
                ans += int(i) ** 2
            if ans == 1:
                return True
            if ans == 2:
                return False
            n = ans
        return False

