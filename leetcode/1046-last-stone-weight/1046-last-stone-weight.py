class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        nums = [-i for i in stones]
        heapq.heapify(nums)

        while len(nums) > 1:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            
            temp = x-y

            heapq.heappush(nums, temp)
        
        return abs(nums[0]) 