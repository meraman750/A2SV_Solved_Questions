class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dec = deque()       
        ans = []
        left = 0
        for i in range(len(nums)):
            while dec and dec[-1] < nums[i]:
                dec.pop()
            dec.append(nums[i])

            if i-left+1 > k: 
                if dec[0] == nums[left]:
                    dec.popleft()
                left+=1
            if i-left+1 == k:
                ans.append(dec[0])
        return ans


