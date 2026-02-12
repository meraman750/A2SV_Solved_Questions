class Solution:
    def frequencySort(self, s: str) -> str:
        d = Counter(s)
        
        sorted_s = sorted(d, key=lambda x: d[x], reverse=True)
        ans = []
        for i in sorted_s:
            ans.extend([i] * d[i])
        return "".join(ans)
