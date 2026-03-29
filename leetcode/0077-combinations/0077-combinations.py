class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        count = 1
        ans = []

        def adder(index, temp):
            if temp and len(temp) == k:
                ans.append(temp[:])
                return 

            for i in range(index, n+1):
                temp.append(i)
                adder(i+1, temp)
                temp.pop()

        adder(1, [])
        return ans