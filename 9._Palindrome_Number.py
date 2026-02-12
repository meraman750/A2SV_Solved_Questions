class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        num = 0
        while temp > 0:
            num = (num * 10) + (temp % 10)
            temp //= 10
        return x == num
