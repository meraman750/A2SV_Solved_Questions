class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        temp = []
        def calc(n):
            if n >= len(nums):
                return 

            for i in range(n, len(nums)):
                temp.append(nums[i])

                if len(temp) >= 2:
                    if temp[-1] < temp[-2]:
                        temp.pop()
                        continue
                    ans.append(temp[:])
                calc(i+1)
                temp.pop()
        calc(0)
        return [list(x) for x in set(tuple(x) for x in ans)]