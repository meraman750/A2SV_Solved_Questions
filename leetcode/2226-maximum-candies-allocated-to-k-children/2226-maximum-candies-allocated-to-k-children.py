class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left = 1
        right = max(candies)
        res = 0

        while left <= right:
            mid = (left+right) // 2

            count = 0
            for i in candies:
                count += (i//mid)
            if count >= k:
                res = mid
                left = mid+1
            else:
                right = mid-1
        return res
