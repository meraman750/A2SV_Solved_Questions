class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        temp = Counter(words)

        ans = sorted(temp, key=lambda x: (-temp[x], x))
        return ans[:k]