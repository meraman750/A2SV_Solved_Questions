class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)

        n = sorted(c.keys(), key=lambda x: (c[x]), reverse=True)
        return n[:k]