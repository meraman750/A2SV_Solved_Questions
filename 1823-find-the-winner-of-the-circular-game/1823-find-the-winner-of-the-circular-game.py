class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        array = []
        for i in range(1, n+1):
            array.append(i)
        i = 0
        while len(array) > 1:
            i = ((i+k-1) % len(array))
            del array[i] 

        return array[0]
         
            