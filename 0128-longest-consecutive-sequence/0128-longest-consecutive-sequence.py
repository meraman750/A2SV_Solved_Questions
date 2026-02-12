class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for i in nums:
            if i - 1 not in nums:
                k = 1
                while i +k in nums:
                    k+=1
                res = max(res, k)
        return res
