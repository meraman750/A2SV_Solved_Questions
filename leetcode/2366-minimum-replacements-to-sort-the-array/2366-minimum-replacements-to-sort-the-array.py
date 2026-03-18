class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        right = nums[-1]
        ans = 0
        for i in range(len(nums)-2, -1, -1):
            left = nums[i]

            while left > right:
                x = ceil(left / right)
                ans+=(x-1)
                left //= x
            right = left
        return ans
            
                # x = ceil(left / 2)
                # y = left - x
                # if x > right:
                #     y+= (x-right)
                #     x-= (x-right)
                # left = y
                # right = x
   