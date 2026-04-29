class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=0
        n=len(nums)-1
        r=len(nums)-1
        first =-1
        last=-1
        while r >= l:
            mid = (l+r) //2
            if nums[mid] == target:
               i, j = mid, mid
               while i>=0 and nums[i] == target:
                first = i
                i-=1
               while j<=n and nums[j] == target:
                last = j
                j+=1
               return first, last  
            elif nums[mid] > target:
                r = mid-1
            else:
                l = mid+1
        return first, last