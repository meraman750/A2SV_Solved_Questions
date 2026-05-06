class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-i for i in piles]
        heapq.heapify(piles)
        while k > 0:
            cur = heapq.heappop(piles)
            # print(cur)
            cur = (cur//2)
            # print(cur)
            heapq.heappush(piles, cur)
            k-=1
            # print(piles)
        piles = [-i for i in piles]
        return sum(piles)
