class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def calc(mid):
            temp = 0
            count = 1
            n = 0
            while n < len(weights):
                if temp + weights[n] <= mid:
                    temp += weights[n]
                else:
                    temp = weights[n]
                    count +=1
                n+=1

            return count <= days
                

        left = max(weights)
        right = sum(weights)
        
        while left < right:
            mid = (left+right) //2
            
            if calc(mid):
                right = mid
            else:
                left = mid+1

        return right