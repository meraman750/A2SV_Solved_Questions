class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMost(k):
            left = 0
            s = defaultdict(int)
            ans = 0
            i = 0
            while i < len(nums):
                s[nums[i]] +=1
                while len(s) > k:
                    s[nums[left]]-=1
                    
                    if s[nums[left]] == 0:
                        del s[nums[left]]
                    
                    left+=1

                ans+= (i-left+1)
                i+=1
            return ans
        return atMost(k) - atMost(k-1)