class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d = Counter(nums)
        idx = 0
        nums[:] = []
        for i in range(0, 4):
            nums.extend([i] * d[i])