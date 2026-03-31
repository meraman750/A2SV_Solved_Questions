class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        temp = []

        def calc(n):
            # if sorted(temp) not in ans:
            ans.add(tuple(sorted((temp[:]))))

            for i in range(n, len(nums)):
                temp.append(nums[i])
                calc(i+1)
                temp.pop()

        calc(0)
        return list(ans)