class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        dec = deque()
        inc = deque()
        ans = 0
        left = 0
        for i in range(len(nums)):
            # print(dec)
            while dec and nums[i] > nums[dec[-1]]:
                dec.pop()
            while inc and nums[i] < nums[inc[-1]]:
                inc.pop()
            dec.append(i)
            inc.append(i)
            # print(dec)
            
            while inc and dec and abs(nums[dec[0]] - nums[inc[0]]) > limit:
                if nums[inc[0]] == nums[left]:
                    inc.popleft()
                if nums[dec[0]] == nums[left]:
                    dec.popleft()
                left+=1
            ans = max(ans, i-left+1)
        return ans