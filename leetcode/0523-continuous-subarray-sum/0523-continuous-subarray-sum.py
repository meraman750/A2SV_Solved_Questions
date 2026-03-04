class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # 23 2  4  6  7
        # 23 25 29 35 42
        # 10 

    
        mp = defaultdict(int)

        count = 1
        mp[0] = -1
        summ=0

        for i in range(len(nums)):
            summ+=nums[i]
            if summ%k in mp:
                if i-mp[summ%k] >= 2:
                    return True
            else:
                mp[summ%k] = i

        return False
        
        

