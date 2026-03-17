class Solution:
    def myPow(self, x: float, n: int) -> float:
        def calc(x, n):
            if n == 0:
                return 1
            if n%2 == 0:
                return (calc(x, n//2)) ** 2
            else:
                return x * ((calc(x, n//2)) ** 2)
                
        if n < 0:
            return calc(1/x, abs(n))
        return calc(x, n)        