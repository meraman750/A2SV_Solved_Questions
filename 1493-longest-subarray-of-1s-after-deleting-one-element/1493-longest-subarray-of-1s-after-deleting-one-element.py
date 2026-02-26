class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if set(nums) == {1}:
            return len(nums)-1

        left = 0
        ans = 0
        flag = True
        count = defaultdict(int)
        for i in range(len(nums)):
            count[nums[i]] +=1
            while count[0] > 1:
                count[nums[left]]-=1
                left+=1
            ans = max(ans, count[1])
            

        return ans

