class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if set(nums) == {0}:
            return "0"
        s = []
        for i in nums:
            s.append(str(i))

        s.sort(key=lambda x: x*10, reverse=True)
        return "".join(s)

