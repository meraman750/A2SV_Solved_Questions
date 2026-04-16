class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = set()

        left = 0
        while left < len(nums):
            
            if nums[left] != left+1:
                if nums[nums[left]-1] == nums[left]:
                    ans.add(nums[left])
                    left+=1
                else:
                    nums[nums[left]-1], nums[left] = nums[left], nums[nums[left]-1]
            else:
                left+=1
        return list(ans)