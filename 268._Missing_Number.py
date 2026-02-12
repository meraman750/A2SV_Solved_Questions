class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i=0
        n = len(nums)
        while i < n:
            c = nums[i]
            if nums[i] < n and nums[i] != nums[c]:
                nums[i], nums[c] = nums[c], nums[i] 
            else:
                i+=1
        for i in range(n):
            if nums[i] != i:
                return i
        return n
