class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left = 0
        while left < len(nums):
            print(left)
            if nums[left] != left+1:
                if nums[nums[left]-1] == nums[left]:
                    return nums[left]
                nums[nums[left]-1], nums[left] = nums[left], nums[nums[left]-1]
            else:
                left+=1
        