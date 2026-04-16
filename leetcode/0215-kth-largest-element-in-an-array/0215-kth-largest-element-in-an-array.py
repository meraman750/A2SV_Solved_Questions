class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        mi = min(nums)
        ma = max(nums)
        ans = [0] * (ma-mi+1)

        for i in range(len(nums)):
            ans[nums[i] - mi] +=1 

        # print(ans)
        count = 0 
        for i in range(len(ans)-1, -1 , -1):
            count+=ans[i]
            if count >= k:
                return mi+i
        
