class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        left = 0
        while left < len(nums):
            temp = nums[left]-1
            if nums[left] > 0 and nums[left] <= len(nums) and nums[left] != nums[temp]:
                nums[left], nums[temp] = nums[temp], nums[left]
            else:
                left+=1
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums)+1
