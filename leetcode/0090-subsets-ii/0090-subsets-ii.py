class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        temp = []

        def calc(n):
            if sorted(temp) not in ans:
                ans.append(sorted(temp[:])) 

            for i in range(n, len(nums)):
                temp.append(nums[i])
                # ans.append(temp)
                calc(i+1)
                temp.pop()

        calc(0)
        return ans