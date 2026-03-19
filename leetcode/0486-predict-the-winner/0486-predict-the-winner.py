class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        def calc(i, j, nums, flag):
            if i == j:
                return nums[i]
            if flag:
                return max(nums[i] + calc(i+1, j, nums, not flag), nums[j] + calc(i, j-1, nums, not flag))

            return min(calc(i+1, j, nums, not flag) - nums[i], calc(i, j-1, nums, not flag) - nums[j])

        return calc(0, len(nums)-1, nums, True) >= 0
            