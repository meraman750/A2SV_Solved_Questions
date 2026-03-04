class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [nums[0]]
        for i in range(1, len(nums)):
            pre.append(pre[-1] * nums[i])
        suf = [nums[-1]]
        for i in range(len(nums)-2, -1, -1):
            suf.append(suf[-1] * nums[i])
        suf.reverse()
        # print(suf)
        # print(pre)

        ans = []
        for i in range(len(nums)):
            if i-1 >= 0 and i+1 < len(nums):
                ans.append(pre[i-1] * suf[i+1])
            elif i-1 < 0:
                ans.append(suf[i+1])
            elif i+1 == len(nums):
                ans.append(pre[i-1])
        return ans
