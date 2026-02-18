class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = [] #1 2 2 3 8
        temp = sorted(nums)
        d = {}
        
        d[temp[0]]=0
        for i in range(1, len(temp)):
            if temp[i] == temp[i-1]:
                continue
            d[temp[i]] = i
        
        for i in range(len(nums)):
            ans.append(d[nums[i]])
        return ans
