class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        dec = []
        minn = nums[0]
        for i in range(len(nums)):
            while dec and nums[i] >= dec[-1][0]:
                dec.pop()
            if dec and nums[i] > dec[-1][1]:
                return True
            
            dec.append([nums[i], minn])
            minn = min(minn, nums[i])
            
        return False
