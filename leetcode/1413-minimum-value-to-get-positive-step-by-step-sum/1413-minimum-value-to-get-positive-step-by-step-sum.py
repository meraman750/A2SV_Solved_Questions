class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minn = float("inf")
        sm = 0
        for i in range(len(nums)):
            sm += nums[i]
            minn = min(minn, sm)

        if minn > 0:
            return 1
        else:
            return (0 - minn + 1)