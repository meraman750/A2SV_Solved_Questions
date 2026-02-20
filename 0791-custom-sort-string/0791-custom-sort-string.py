class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)
        ans = []
        for i in order:
            if i in s:
                ans.append(i * count[i])
                del count[i]
        for key, val in count.items():
            ans.append(key * val)

        return "".join(ans)
