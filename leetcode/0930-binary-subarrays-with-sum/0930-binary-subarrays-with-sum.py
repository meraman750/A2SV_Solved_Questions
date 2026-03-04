class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        if len(nums) == 1 and nums[0] != k:
            return 0
        pre = [nums[0]]
        for i in range(1, len(nums)):
            pre.append(pre[-1] + nums[i])

        ans = 0
        prev = defaultdict(int)
        for i in pre:
            ans+= prev[i-goal]
            if i == goal:
                ans+=1
            prev[i] +=1
        
        return ans