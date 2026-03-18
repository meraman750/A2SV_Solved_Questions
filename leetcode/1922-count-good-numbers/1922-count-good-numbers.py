class Solution:
    def countGoodNumbers(self, n: int) -> int:
        if n % 2 == 0:
            return mod(pow(4, (n//2), (10 ** 9) + 7) * pow(5, (n//2), (10 ** 9) + 7), (10 ** 9) + 7)
        return mod(pow(4, (n-ceil(n/2)), (10 ** 9) + 7) * pow(5, (ceil(n/2)), (10 ** 9) + 7), (10 ** 9) + 7) 
        
