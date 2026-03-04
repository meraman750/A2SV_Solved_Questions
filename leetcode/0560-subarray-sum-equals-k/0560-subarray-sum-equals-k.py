class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        if len(nums) == 1 and nums[0] != k:
            return 0
        pre = [nums[0]]
        for i in range(1, len(nums)):
            pre.append(pre[-1] + nums[i])

        ans = 0
        prev = defaultdict(int)
        for i in pre:
            ans+= prev[i-k]
            if i == k:
                ans+=1
            prev[i] +=1
        
        return ans
            