class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        temp = []

        def calc(n):
            if len(temp) == len(nums):
                ans.append(temp[:])
                return 

            for i in range(n, len(nums)):
                if nums[i] not in temp:
                    temp.append(nums[i])
                    calc(0)
                    temp.pop()

        calc(0)
        return ans

