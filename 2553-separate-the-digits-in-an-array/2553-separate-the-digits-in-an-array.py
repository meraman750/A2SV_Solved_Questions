class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []

        for i in nums:
            x = str(i)
            for j in x:
                ans.append(int(j))
        return ans
