class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums.count(0) == 0:
            return True
        cur = len(nums)-1
        
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= cur:
                cur = i
        if cur == 0:
            return True
        return False
