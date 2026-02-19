class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        ans = 0
        count = 0
        amount = len(piles) // 3
        for i in range(1, len(piles)-amount, 2):
            # if count == amount:
            #     break
            ans += piles[i]
            # count+=1
        return ans
