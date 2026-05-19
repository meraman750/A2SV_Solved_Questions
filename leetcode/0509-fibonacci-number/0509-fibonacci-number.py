class Solution:
    memo = {}
    def fib(self, n: int) -> int:
        if n == 1 or n== 0:
            return n
        if n not in self.memo:
            self.memo[n] = self.fib(n-1) + self.fib(n-2)

        return self.memo[n]
        
        # def calc(n):
        #     if n == 1:
        #         return 1
        #     if n == 0:
        #         return 0
            
        #     return calc(n-2) + calc(n-1)
        
        # return calc(n)