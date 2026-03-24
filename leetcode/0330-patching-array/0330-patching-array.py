class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        ans = 0
        miss = 1
        i = 0
        while miss <= n:
            if len(nums) > i and miss >= nums[i]:
                miss += nums[i]
                i+=1
            else:
                ans+=1
                miss *=2
        return ans