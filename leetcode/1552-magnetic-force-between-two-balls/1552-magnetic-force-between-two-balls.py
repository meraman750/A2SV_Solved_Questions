class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def calc(n):
            last = position[0]
            count=1
            for i in range(1, len(position)):
                if position[i] - last >= n:
                    count+=1
                    last = position[i]
                if count >= m:
                    return True
            return count >= m

        left = 1
        right = position[-1] - position[0]
        ans = 0
        while left <= right:
            mid = (left+right) // 2
            
            if calc(mid):
                ans = mid
                left = mid+1
            else:
                right = mid-1
        return ans
            
