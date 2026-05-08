class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        nums = []
        for i in matrix:
            for j in i:
                nums.append(j)

        heapq.heapify(nums)
        while k > 1:
            heapq.heappop(nums)
            k-=1
        print(nums)
        return nums[0]
