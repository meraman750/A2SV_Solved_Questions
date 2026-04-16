class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # nums.sort()
        # flag = False
        # ans = []
        # for i in range(len(nums)-1):
        #     if nums[i] +1 != nums[i+1]:
        #         ans.append(nums[i]+1)
        #         flag = True
        # if flag:
        new_nums = set(nums)
        for i in range(1, 2 ** 31):
            if i not in new_nums:
                return i

             