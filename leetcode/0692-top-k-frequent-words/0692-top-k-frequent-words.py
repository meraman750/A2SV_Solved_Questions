class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)

        heap = []
        for key, val in count.items():
            heapq.heappush(heap, [-val, key])

        ans = []
        while k:
            ans.append(heapq.heappop(heap)[1])
            k-=1
        return ans